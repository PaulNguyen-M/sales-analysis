import numpy as np
import pandas as pd

def add_feature(df):

    df['Ngay_Xuat'] = pd.to_datetime(df['Ngay_Xuat'], errors='coerce')

    df['Profit'] = df['Doanh_Thu'] - df['Tien_Nhap']
    df['Month'] = df['Ngay_Xuat'].dt.month
    df['Promo'] = df['SL_Xuat_KM'] > 0

    df['Revenue'] = np.where(df['SL_Xuat'] > 0, df['Doanh_Thu'] / df['SL_Xuat'], 0)
    return df