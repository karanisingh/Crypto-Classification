# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import snscrape.modules.twitter as sntwitter
import pandas as pd
import time
import threading

# Threaded function to get last 10000 tweets from each month
def get_10000_tweets(start, end, result, index):
    tweets_100 = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'bitcoin $BTC since:{start} until:{end}').get_items()):
        if i > 10000:
            break
        tweets_100.append([tweet.date, 
                             tweet.content, 
                             tweet.user.verified, 
                             tweet.user.followersCount,
                             tweet.user.friendsCount,
                             tweet.likeCount,
                             tweet.retweetCount,
                             tweet.replyCount,
                             tweet.lang,
                             ])
    result[index] = tweets_100

    
results = [0]*48
tic = time.perf_counter()

# Threading Fun
t1 = threading.Thread(target=get_10000_tweets, args=('2018-01-01', '2018-01-31',results, 0)); t1.start()
t2 = threading.Thread(target=get_10000_tweets, args=('2018-02-01', '2018-02-28',results, 1)); t2.start()  
t3 = threading.Thread(target=get_10000_tweets, args=('2018-03-01', '2018-03-31',results, 2)); t3.start()  
t4 = threading.Thread(target=get_10000_tweets, args=('2018-04-01', '2018-04-30',results, 3)); t4.start()  
t5 = threading.Thread(target=get_10000_tweets, args=('2018-05-01', '2018-05-31',results, 4)); t5.start()  
t6 = threading.Thread(target=get_10000_tweets, args=('2018-06-01', '2018-06-30',results, 5)); t6.start()  
t7 = threading.Thread(target=get_10000_tweets, args=('2018-07-01', '2018-07-31',results, 6)); t7.start()  
t8 = threading.Thread(target=get_10000_tweets, args=('2018-08-01', '2018-08-31',results, 7)); t8.start()  
t9 = threading.Thread(target=get_10000_tweets, args=('2018-09-01', '2018-09-30',results, 8)); t9.start()  
t10= threading.Thread(target=get_10000_tweets, args=('2018-10-01', '2018-10-31',results, 9)); t10.start()  
t11=threading.Thread(target=get_10000_tweets, args=('2018-11-01', '2018-11-30',results, 10)); t11.start()  
t12=threading.Thread(target=get_10000_tweets, args=('2018-12-01', '2018-12-31',results, 11)); t12.start()
t13=threading.Thread(target=get_10000_tweets, args=('2019-01-01', '2019-01-31',results, 12)); t13.start()
t14=threading.Thread(target=get_10000_tweets, args=('2019-02-01', '2019-02-28',results, 13)); t14.start()  
t15=threading.Thread(target=get_10000_tweets, args=('2019-03-01', '2019-03-31',results, 14)); t15.start()  
t16=threading.Thread(target=get_10000_tweets, args=('2019-04-01', '2019-04-30',results, 15)); t16.start()  
t17=threading.Thread(target=get_10000_tweets, args=('2019-05-01', '2019-05-31',results, 16)); t17.start()  
t18=threading.Thread(target=get_10000_tweets, args=('2019-06-01', '2019-06-30',results, 17)); t18.start()  
t19=threading.Thread(target=get_10000_tweets, args=('2019-07-01', '2019-07-31',results, 18)); t19.start()  
t20=threading.Thread(target=get_10000_tweets, args=('2019-08-01', '2019-08-31',results, 19)); t20.start()  
t21=threading.Thread(target=get_10000_tweets, args=('2019-09-01', '2019-09-30',results, 20)); t21.start()  
t22=threading.Thread(target=get_10000_tweets, args=('2019-10-01', '2019-10-31',results, 21)); t22.start()  
t23=threading.Thread(target=get_10000_tweets, args=('2019-11-01', '2019-11-30',results, 22)); t23.start()  
t24=threading.Thread(target=get_10000_tweets, args=('2019-12-01', '2019-12-31',results, 23)); t24.start()
t25=threading.Thread(target=get_10000_tweets, args=('2020-01-01', '2020-01-31',results, 24)); t25.start()
t26=threading.Thread(target=get_10000_tweets, args=('2020-02-01', '2020-02-29',results, 25)); t26.start()  
t27=threading.Thread(target=get_10000_tweets, args=('2020-03-01', '2020-03-31',results, 26)); t27.start()  
t28=threading.Thread(target=get_10000_tweets, args=('2020-04-01', '2020-04-30',results, 27)); t28.start()  
t29=threading.Thread(target=get_10000_tweets, args=('2020-05-01', '2020-05-31',results, 28)); t29.start()  
t30=threading.Thread(target=get_10000_tweets, args=('2020-06-01', '2020-06-30',results, 29)); t30.start()  
t31=threading.Thread(target=get_10000_tweets, args=('2020-07-01', '2020-07-31',results, 30)); t31.start()  
t32=threading.Thread(target=get_10000_tweets, args=('2020-08-01', '2020-08-31',results, 31)); t32.start()  
t33=threading.Thread(target=get_10000_tweets, args=('2020-09-01', '2020-09-30',results, 32)); t33.start()  
t34=threading.Thread(target=get_10000_tweets, args=('2020-10-01', '2018-10-31',results, 33)); t34.start()  
t35=threading.Thread(target=get_10000_tweets, args=('2020-11-01', '2020-11-30',results, 34)); t35.start()  
t36=threading.Thread(target=get_10000_tweets, args=('2020-12-01', '2020-12-31',results, 35)); t36.start()  
t37=threading.Thread(target=get_10000_tweets, args=('2021-01-01', '2021-01-31',results, 36)); t37.start()
t38=threading.Thread(target=get_10000_tweets, args=('2021-02-01', '2021-02-28',results, 37)); t38.start()  
t39=threading.Thread(target=get_10000_tweets, args=('2021-03-01', '2021-03-31',results, 38)); t39.start()  
t40=threading.Thread(target=get_10000_tweets, args=('2021-04-01', '2021-04-30',results, 39)); t40.start()  
t41=threading.Thread(target=get_10000_tweets, args=('2021-05-01', '2021-05-31',results, 40)); t41.start()  
t42=threading.Thread(target=get_10000_tweets, args=('2021-06-01', '2021-06-30',results, 41)); t42.start()  
t43=threading.Thread(target=get_10000_tweets, args=('2021-07-01', '2021-07-31',results, 42)); t43.start()  
t44=threading.Thread(target=get_10000_tweets, args=('2021-08-01', '2021-08-31',results, 43)); t44.start()  
t45=threading.Thread(target=get_10000_tweets, args=('2021-09-01', '2021-09-30',results, 44)); t45.start()  
t46=threading.Thread(target=get_10000_tweets, args=('2021-10-01', '2021-10-31',results, 45)); t46.start()  
t47=threading.Thread(target=get_10000_tweets, args=('2021-11-01', '2021-11-30',results, 46)); t47.start()  
t48=threading.Thread(target=get_10000_tweets, args=('2021-12-01', '2021-12-15',results, 47)); t48.start()           

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()
t11.join()
t12.join()
t13.join()
t14.join()
t15.join()
t16.join()
t17.join()
t18.join()
t19.join()
t20.join()
t21.join()
t22.join()
t23.join()
t24.join()
t25.join()
t26.join()
t27.join()
t28.join()
t29.join()
t30.join()
t31.join()
t32.join()
t33.join()
t34.join()
t35.join()
t36.join()
t37.join()
t38.join()
t39.join()
t40.join()
t41.join()
t42.join()
t43.join()
t44.join()
t45.join()
t46.join()
t47.join()
t48.join()

# Combine the results from the thread
joined_tweets = results[0]
for i in range(1,48):
    joined_tweets = joined_tweets + results[i]

# Create the data frame
joined_tweets = pd.DataFrame(joined_tweets, 
                          columns=['Datetime', 
                                   'Text', 
                                   'Verified?', 
                                   'Followers',
                                   'Friends',
                                   'Likes',
                                   'Retweets',
                                   'Replies',
                                   'Language'
                                   ])

# Extract as csv to then use for data wrangling
joined_tweets.to_csv('test.csv')

