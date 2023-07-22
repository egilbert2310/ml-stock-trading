import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split



def load_data(laptop = True):
    lap_top_data_fp = "C:/Users/student/Documents/ml-stock-trading/data/individual_stocks_5yr/individual_stocks_5yr/AAPL_data.csv"
    desk_top_data_fp = "C:/Users/Eric/Documents/ml-stock-trading/data/individual_stocks_5yr/individual_stocks_5yr/AAPL_data.csv"
    if laptop:
        df = pd.read_csv(lap_top_data_fp)
    else:
        df = pd.read_csv(desk_top_data_fp)
    return df


def prep_data(df):

    df['date'] = pd.to_datetime(df['date'])
    df['local_min'] = df.close[(df.close.shift(1) > df.close) & (df.close.shift(-1) > df.close)]
    df['local_max'] = df.close[(df.close.shift(1) < df.close) & (df.close.shift(-1) < df.close)]
    df['min_binary'] = df['local_min'].notnull()
    df['max_binary'] = df['local_max'].notnull()
    df['normalized_value'] = (df['close'] - df['low'] / df['high'] - df['low'])
    df['target'] = df['local_min'].notnull()*1


    return df