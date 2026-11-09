"""Protocol invariants and input-corruption checks; no competition data needed."""
from pathlib import Path
import sys
import unittest

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from person_b import (nested_stratified_indices, select_pseudo_labels,
                      validate_split_data)


class ProtocolTests(unittest.TestCase):
    def test_nested_balanced_subsets_are_reproducible(self):
        labels = np.tile([0, 1], 4000)
        sizes = [500, 1000, 2000, 5000, 8000]
        first = nested_stratified_indices(labels, sizes, 42)
        second = nested_stratified_indices(labels, sizes, 42)
        previous = set()
        for size in sizes:
            selected = first[size]
            self.assertEqual(len(selected), size)
            self.assertEqual(len(set(selected)), size)
            self.assertEqual(np.bincount(labels[selected]).tolist(), [size//2, size//2])
            self.assertTrue(previous.issubset(set(selected)))
            np.testing.assert_array_equal(selected, second[size])
            previous = set(selected)
        np.testing.assert_array_equal(first[8000], np.arange(8000))

    def test_confidence_boundary_and_class_orientation(self):
        selected, labels = select_pseudo_labels([0, .05, .051, .5, .949, .95, 1], .05, .95)
        np.testing.assert_array_equal(selected, [True, True, False, False, False, True, True])
        np.testing.assert_array_equal(labels, [0, 0, 1, 1])

    def test_invalid_probabilities_and_thresholds_fail(self):
        for probabilities in ([np.nan], [1.1], [-.1], [[.1, .9]]):
            with self.assertRaises(ValueError):
                select_pseudo_labels(probabilities, .05, .95)
        with self.assertRaises(ValueError):
            select_pseudo_labels([.1], .6, .9)

    def test_empty_confidence_selection_is_supported(self):
        selected, labels = select_pseudo_labels([.2, .5, .8], .05, .95)
        self.assertFalse(selected.any())
        self.assertEqual(len(labels), 0)

    def test_mismatched_labels_unknown_ids_and_duplicate_ids_fail(self):
        train = pd.DataFrame({"id": ["a", "b", "c", "d"], "label": [0, 1, 0, 1]})
        valid = train.assign(random_fold=["train", "train", "val", "val"],
                             cluster=[0, 0, 1, 1],
                             ood_fold=["train", "train", "val", "val"])
        validate_split_data(train, valid)
        for column, value in [("label", 1), ("id", "unknown"), ("random_fold", "invalid")]:
            bad = valid.copy()
            bad.loc[0, column] = value
            with self.assertRaises(ValueError):
                validate_split_data(train, bad)
        bad = valid.copy()
        bad.loc[0, "id"] = "b"
        with self.assertRaises(ValueError):
            validate_split_data(train, bad)


if __name__ == "__main__":
    unittest.main()
