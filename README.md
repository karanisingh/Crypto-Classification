# Crypto-Classification

This project was created for the class CS 4501: Statistical Learning and Graphical Models. I aim to see if daily price change in Bitcoin can be predicted by historic pubilc sentiment as measured from Twitter data. Specifically, will the average number of likes and hashtags per tweet including 'Bitcoin' or '$BTC'.

## Introduction

In stock market investing, the Efficient Market Hypothess states that markets are efficient to an extent that investment strategies are futile in making gains beyond where the overall market moves. Cryptocurrency markets have significantly less data and their efficiency is less tested. This project aims to challenge the efficiency of the Bitcoin market by testing its predictability, specifically, using public sentiment on social media as a predictor. *Can daily price changes in Bitcoin be predicted by twitter sentiment from the previous day?*

## Data

Raw data was collected by using **snscrape**, a social networking site scraper (repository link here: https://github.com/JustAnotherArchivist/snscrape). I used this along with multithreading to be able to collect more than 470,000 tweets containing 'bitcoin' or '$BTC'. Also used was daily price chaing collected from www.statista.com to be able to determine if Bitcoin increased or decreased in price for a day. 

After data manipulation, our final data included the min-max-normalized average number of likes and retweets per tweet including the phrases above for the last handful of days each month for the past three years along with if the price for Bitcoin increased or decreased the next day.

I chose these two metrics as a result of intuition: the more likes a tweet receives, the more there is support for the tweet, and also the more outreach a tweet has. Also, the more hashtags there are in a tweet, the more outreach that tweet has to people that may not be a part of that tweet creator's network. So, the more likes and hashtags there are could potentially show sentiment for a vast amount of people.

## Methods

Used many linear classification models.

The first classification model utlized maximum likelihood for Linear Discriminant Analysis. With the data, I was able to use Maximum Likelihood strategy to estimate the mean for each class and the covariance. Once this was obtained, I could calculate the decision boundary.

The second classification model was a discriminative model that used logistic regression. To be able to estimate the parameters needed to create the decision boundary, I used both Gradient Descent and Stochastic Gradient Descent. Once this was found, I was able to create the decision boundary.

## Conclusion

This was totally, completely, utturly, absolutely, wholly inconclusive. It comes to no surprise that it is not possible to predict a cryptocurrency's value from very basic twitter data.

If I were to further improve this project, I would likely start by making the multithreading process more efficient to be able to obtain more data across a longer time period. I would also try to pick different metrics, and possible run the same models on different combinations of metrics.
