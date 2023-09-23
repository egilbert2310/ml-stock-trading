from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
import pandas as pd

## REVISIONS ##
# Need to be able to choose which linear model I want to use
# Need to do a gridsearch to choose the optimal parameters for which model I choose
# (Including comparing R^2 scores to determine the best model)
# Create a dataframe of coefs from the best model created (from the model that was intiailly chosen)















class StockLinearModel:
    def __init__(self, linear_regression = True, ridge = False):
        """
        Default is Linear Regression
        """
        self.linear_regression = linear_regression
        self.ridge = ridge
        if self.ridge == True:
            self.linear_regression == False



    def choosing_linear_model(self, X, y):
        if self.linear_regression == True:
           
           return  

    # def create_coef_data(self, df, days):
    #     data = {}
    #     for day in days:
    #         n_day_values = self.creating_n_day_dfs(df=df, n=day)
    #         n_day_coef_s = self.n_day_linear_regression(n_day_values=n_day_values)
    #         col_name = f"{day}_day_linear_regression"
    #         data[col_name] = n_day_coef_s
    #     coef_df = pd.DataFrame(data=data)
    #     return coef_df

    # def n_day_linear_regression(self, n_day_values):
    #     n_day_coef_s = []
    #     for df in n_day_values:
    #         X = df.date.values.reshape(-1, 1)
    #         y = df.close.values
    #         coef_ = self.linear_regression_coefs(X=X, y=y)
    #         n_day_coef_s.append(coef_)
            
    #     return n_day_coef_s

    def linear_regression_coefs(self, X, y):
        linear_regression = LinearRegression().fit(X, y)
        return linear_regression.coef_[0]

    def ridge_regression_coefs(self, X, y, alpha):
        ridge_regression = Ridge(alpha=alpha).fit(X, y)
        return ridge_regression.coef_[0]


    def creating_n_day_dfs(self, df, n):
        necessary_cols = df[["date", "close"]]
        n_day_values = []
        for i in range(len(necessary_cols)):
            try:
                df_slice = necessary_cols[i : i + n]
                n_day_values.append(df_slice)
            except:
                break
        return n_day_values
