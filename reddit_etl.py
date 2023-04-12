import pandas as pd 
import s3fs
import json
from datetime import datetime
import requests

def reddit_extract():
    headers = {
    'User-Agent' : '(Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15)'
    }
    
    urls = [
        'https://www.reddit.com/r/elon/comments.json?limit=100', 
        'https://www.reddit.com/r/elonmusk/comments.json?limit=100'
    ]
    
    df_list = list()

    for url in urls:
        response = requests.get(url, headers = headers).json()

        sub_reddits = [sub['data']['link_title'] for sub in response['data']['children']]
        sub_ids = [sub['data']['subreddit_id'] for sub in response['data']['children']]
        sub_utc = [datetime.utcfromtimestamp(sub['data']['created_utc']) for sub in response['data']['children']]
        user_ids = [sub['data']['link_author'] for sub in response['data']['children']]
        sub_ups = [sub['data']['ups'] for sub in response['data']['children']]

        sub_info = list(zip(sub_ids, user_ids, sub_reddits, sub_ups, sub_utc))

        sub_df = pd.DataFrame(sub_info, columns = ['sub_ids', 'user_ids', 'sub_reddits', 'sub_ups', 'sub_utc'])

        df_list.append(sub_df)

    df = pd.concat(df_list)
    df.reset_index(inplace = True, drop = True)

    df.to_csv('s3://etl-reddit-bucket/reddit_data.csv', index = False)

