class Transformer:

    def fit(self, X, y=None):
        raise NotImplementedError

    def transform(self, X):
        raise NotImplementedError

    def fit_transform(self, X, y=None):
        self.fit(X, y)
        return self.transform(X)