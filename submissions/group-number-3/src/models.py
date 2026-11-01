"""Model definitions. Add new models here as functions returning sklearn estimators."""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import FeatureUnion, Pipeline


def tfidf_logreg(C=4.0):
    """Baseline: word 1-2 grams + char 3-5 grams TF-IDF -> logistic regression."""
    features = FeatureUnion([
        ("word", TfidfVectorizer(analyzer="word", ngram_range=(1, 2),
                                 min_df=2, max_features=200_000,
                                 sublinear_tf=True)),
        ("char", TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5),
                                 min_df=3, max_features=300_000,
                                 sublinear_tf=True)),
    ])
    return Pipeline([
        ("features", features),
        ("clf", LogisticRegression(C=C, max_iter=2000)),
    ])


MODELS = {
    "tfidf_logreg": tfidf_logreg,
}
