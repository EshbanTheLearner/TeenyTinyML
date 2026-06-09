from abc import abstractmethod
from .estimator import BaseEstimator


class Classifier(BaseEstimator):

    @abstractmethod
    def fit(self, X, y):
        pass

    @abstractmethod
    def predict(self, X):
        pass

    def predict_proba(self, X):
        raise NotImplementedError