from sklearn.linear_model import LinearRegression


class StockLinearRegression:
    def __init__(self) -> None:
        pass

    def linear_regression_coefs(self, X, y):
        linear_regression = LinearRegression().fit(X, y)

        return linear_regression.coef_
