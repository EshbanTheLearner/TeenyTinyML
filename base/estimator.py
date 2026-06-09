from abc import ABC, abstractmethod

class BaseEstimator(ABC):
    """
        Parent class for all TeenyTinyML objects.
    """

    def get_params(self):
        return self.__dict__

    def set_params(self, **params):
        for k, v in params.items():
            setattr(self, k, v)
        return self