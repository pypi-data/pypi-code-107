from abc import ABCMeta, abstractmethod

from sklearn.base import (
    BaseEstimator,
    ClassifierMixin,
    RegressorMixin,
    TransformerMixin,
)


class BaseClassifier(BaseEstimator, ClassifierMixin, metaclass=ABCMeta):
    @abstractmethod
    def fit(self, X, y) -> "BaseClassifier":
        raise NotImplementedError

    @abstractmethod
    def predict(self, X):
        raise NotImplementedError


class BaseRegressor(BaseEstimator, RegressorMixin, metaclass=ABCMeta):
    @abstractmethod
    def fit(self, X, y) -> "BaseRegressor":
        raise NotImplementedError

    @abstractmethod
    def predict(self, X):
        raise NotImplementedError


class BaseTransformer(BaseEstimator, TransformerMixin, metaclass=ABCMeta):
    def fit(self, X, y=None) -> "BaseTransformer":
        return self

    @abstractmethod
    def transform(self, X):
        raise NotImplementedError
