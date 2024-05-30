import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets['valid'] = tweets['content'].apply(lambda x: '0' if len(x)>15 else '1')
    tweets = tweets[tweets['valid'] == '0']
    tweets = tweets.drop(columns=['content', 'valid'])
    return tweets