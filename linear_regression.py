from sklearn.linear_model import LinearRegression


class StockLinearRegression:
    def __init__(self) -> None:
        pass

    def linear_regression_coefs(self, X, y):
        linear_regression = LinearRegression().fit(X, y)

        return linear_regression.coef_

    def creating_n_day_dfs(self, df, n):
        necessary_cols = df[
            ["date", "open", "high", "low", "close", "volume", "normalized_value"]
        ]
        n_day_values = []

        for i in range(len(necessary_cols)):
            try:
                df_slice = necessary_cols[i : i + n]
                n_day_values.append(df_slice)
            except:
                break
        return n_day_values
