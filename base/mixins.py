from abc import abstractmethod


class TransformerMixin:
    """
    Adds fit_transform() to transformers.
    """

    def fit_transform(self, X, y=None):
        self.fit(X, y)
        return self.transform(X)


class PredictorMixin:
    """
    Adds score() using model predictions.
    """

    def score(self, X, y):
        raise NotImplementedError


class RegressorMixin(PredictorMixin):
    """
    Default regression scoring.
    Uses R².
    """

    def score(self, X, y):

        y_pred = self.predict(X)

        ss_res = ((y - y_pred) ** 2).sum()
        ss_tot = ((y - y.mean()) ** 2).sum()

        return 1 - (ss_res / ss_tot)


class ClassifierMixin(PredictorMixin):
    """
    Default classification scoring.
    Uses accuracy.
    """

    def score(self, X, y):

        y_pred = self.predict(X)

        return (y_pred == y).mean()


class ProbabilityMixin:
    """
    Indicates support for probabilities.
    """

    @abstractmethod
    def predict_proba(self, X):
        pass


class FittableMixin:
    """
    Utility for checking fit status.
    """

    def _set_fitted(self):
        self._is_fitted = True

    def _check_is_fitted(self):

        if not getattr(self, "_is_fitted", False):
            raise RuntimeError(
                f"{self.__class__.__name__} has not been fitted."
            )