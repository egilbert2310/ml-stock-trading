import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


class DataPrep:
    def __init__(self) -> None:
        pass

    def load_raw_data(self, laptop=True):
        laptop_data_fp = "C:/Users/student/Documents/ml-stock-trading/data/individual_stocks_5yr/individual_stocks_5yr/AAPL_data.csv"
        desktop_data_fp = "C:/Users/Eric/Documents/ml-stock-trading/data/individual_stocks_5yr/individual_stocks_5yr/AAPL_data.csv"
        if laptop:
            df = pd.read_csv(laptop_data_fp)
        else:
            df = pd.read_csv(desktop_data_fp)
        return df

    def prep_raw_data(self, df):
        df["date"] = pd.to_datetime(df["date"])
        df["local_min"] = df.close[
            (df.close.shift(1) > df.close) & (df.close.shift(-1) > df.close)
        ]
        df["local_max"] = df.close[
            (df.close.shift(1) < df.close) & (df.close.shift(-1) < df.close)
        ]
        df["min_binary"] = df["local_min"].notnull()
        df["max_binary"] = df["local_max"].notnull()
        df["normalized_value"] = df["close"] - df["low"] / df["high"] - df["low"]
        df["target"] = df["local_min"].notnull() * 1
        return df

    def prep_training_data(self, coef_df, stock_df):
        training_data = coef_df.copy()
        training_data["normalized_value"] = stock_df["normalized_value"]
        training_data["volume"] = stock_df["volume"]
        training_data["RSI"] = stock_df['RSI']
        training_data["target"] =  stock_df['target']
        training_data = training_data.dropna()
        return training_data

    def calc_rsi(self, df):
        df['pct_change'] = df.close.pct_change() * 100
        df['gain'] = [x if x > 0 else 0 for x in df['pct_change']]
        df['loss'] = [abs(x) if x < 0 else 0 for x in df['pct_change']]
        df['14_avg_gain'] = df.gain.rolling(14).mean()
        df['14_avg_loss'] = df.loss.rolling(14).mean()
        df['RS'] = df['14_avg_gain'] / df['14_avg_loss']
        df['RSI'] = 100 - (100 / (1 + df['RS']))
        return df