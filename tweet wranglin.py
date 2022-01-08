# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 17:49:42 2021

@author: vbmsi

The purpose of this file is to take the raw data (millions of tweets) and
condense it into summaries for each day with the relavant data
"""

import pandas as pd

# Import the raw data
tweets = pd.read_csv('test.csv')

# Remove unnecessary columns
tweets.drop(['Retweeted?', 'Quoted?', 'Source'],
            axis=1,
            inplace=True)

# Remove rows not in enlish
tweets.drop(tweets.index[tweets['Language']!='en'],inplace=True)

# Take away time from datetime
tweets['Datetime'] = tweets['Datetime'].apply(lambda str: str[:10])

# Remove incomplete days
tweets.drop(tweets.index[tweets['Datetime']=='2018-01-26'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2018-02-22'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2018-03-25'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2018-04-24'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2018-05-25'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2018-06-23'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2018-07-25'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2018-08-24'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2018-09-23'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2018-10-23'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2018-11-24'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2018-12-22'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2019-01-21'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2019-02-20'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2019-03-22'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2019-04-22'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2019-05-24'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2019-06-25'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2019-07-23'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2019-08-25'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2019-09-23'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2019-10-25'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2019-11-22'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2019-12-22'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2020-01-24'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2020-02-24'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2020-03-25'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2020-04-24'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2020-05-25'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2020-06-23'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2020-07-26'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2020-08-25'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2020-09-23'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2020-10-26'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2020-11-25'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2020-12-27'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2021-01-28'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2021-02-25'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2021-03-27'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2021-04-26'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2021-05-28'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2021-06-27'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2021-07-28'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2021-08-27'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2021-09-26'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2021-10-28'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2021-11-27'],inplace=True)
tweets.drop(tweets.index[tweets['Datetime']=='2021-12-12'],inplace=True)

# New column for character count (in case we use it)
tweets['Tweet Length'] = tweets.apply(lambda row: len(row.Text), axis=1)

# New column for hashtag count
tweets['Hashtag Count'] = tweets.apply(lambda row: row.Text.count('#'),axis=1)

# Dropping language column since it is irrelevant now
tweets.drop(['Language', 'Unnamed: 0', 'Text'],axis=1,inplace=True)

# Get the average for each day
tweets = tweets.groupby(['Datetime']).mean()

# Normalize using min max and then export for classification
normalized_tweets = (tweets-tweets.min())/(tweets.max()-tweets.min())
tweets.to_csv('tweets_wrangled.csv')
normalized_tweets.to_csv('normalized_tweets_wrangled.csv')

# Import the raw bitcoin data, clean up the dataframe, export for classification
btc = pd.read_csv('btcdata.csv')
btc.drop(['Date'],axis=1,inplace=True)
btc.rename(columns={'Change %' :'Rise?'}, inplace=True)
btc['Rise?'] = btc['Rise?'].apply(lambda hm: 0 if hm[0]=='-' else 1)
btc.to_csv('finalbtc.csv')
