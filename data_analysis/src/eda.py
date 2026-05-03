def revenue_by_product(df):
    return df.groupby('Hang')['Doanh_Thu'].sum().sort_values(ascending=False)

def profit_by_product(df):
    return df.groupby('Hang')['Profit'].sum().sort_values(ascending=False)

def top_customers(df):
    return df.groupby('Khach_Hang')['Doanh_Thu'].sum().sort_values(ascending=False)

def promotion_effect(df):
    return df.groupby('Promo')['Doanh_Thu'].mean()

def revenue_by_month(df):
    return df.groupby('Month')['Doanh_Thu'].sum()