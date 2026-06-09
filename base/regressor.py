from abc import abstractmethod
from .estimator import BaseEstimator


class Regressor(BaseEstimator):

    @abstractmethod
    def fit(self, X, y):
        pass

    @abstractmethod
    def predict(self, X):
        pass