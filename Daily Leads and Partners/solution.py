import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    df_grouped_1 = daily_sales.groupby(['date_id', 'make_name'])['lead_id'].agg([('unique_leads', 'nunique')])
    df_grouped_2 = daily_sales.groupby(['date_id', 'make_name'])['partner_id'].agg([('unique_partners', 'nunique')])
    df_grouped_3 = df_grouped_1.merge(df_grouped_2, on=['date_id', 'make_name'])
    df_grouped_3.reset_index(inplace=True)
    return df_grouped_3