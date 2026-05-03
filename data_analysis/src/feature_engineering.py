import numpy as np

def add_feature(df):
    df['Profit'] = df['Doanh_Thu'] - df['Tien_Nhap']
    df['Month'] = df['Ngay_Xuat'].dt.month
    df['Promo'] = df['SL_Xuat_KM'] > 0

    df['Revenue'] = np.where(df['SL_Xuat'] > 0, df['Doanh_Thu'] / df['SL_Xuat'], 0)
    return df