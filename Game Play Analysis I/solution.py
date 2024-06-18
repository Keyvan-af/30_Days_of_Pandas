import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity_group = activity.groupby("player_id")['event_date'].min().reset_index()
    df = activity_group[['player_id', 'event_date']]
    df.rename(columns={"event_date": "first_login"}, inplace=True)
    return df