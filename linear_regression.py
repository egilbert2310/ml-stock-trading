from sklearn.linear_model import LinearRegression
import pandas as pd

class StockLinearRegression:
    def __init__(self) -> None:
        pass


    def create_coef_data(self,df,days):
        data={}
        for day in days:
            n_day_values = self.creating_n_day_dfs(df=df, n=day)
            n_day_coef_s = self.n_day_linear_regression(n_day_values=n_day_values)
            col_name = f'{day}_day_linear_regression'
            data[col_name] = n_day_coef_s
        coef_df = pd.DataFrame(data=data)
        return coef_df

    def n_day_linear_regression(self, n_day_values):
        n_day_coef_s = []
        for df in n_day_values:
            X = df.date.values.reshape(-1,1)
            y = df.close.values
            coef_ = self.linear_regression_coefs(X=X, y=y)
            n_day_coef_s.append(coef_)
        return n_day_coef_s
    
    def linear_regression_coefs(self, X, y):
        linear_regression = LinearRegression().fit(X, y)
        return linear_regression.coef_[0]

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










    
