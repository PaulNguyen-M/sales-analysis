import pandas as pd

def clean_data(df):
    # Rename columns
    df.columns = [
        'STT', 'Ma', 'Hang', 'DVT', 'Tien_Nhap', 'SL_Xuat_KM', 'SL_Xuat', 'Tien_Xuat', 'Doanh_Thu', 'Ngay_Xuat', 'Khach_Hang' ]
    
    # Convert data
    df['Ngay_Xuat'] = pd.to_datetime(df['Ngay_Xuat'], errors='coerce')

    # drop null
    df = df.dropna(subset=['Hang', 'Doanh_Thu'])

    return df