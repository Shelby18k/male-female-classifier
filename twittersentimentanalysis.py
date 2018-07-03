import tweepy
from textblob import TextBlob
import csv

# with open('tweets.csv','wt') as outcsv:
# 	writer = csv.DictWriter(outcsv,fieldnames=["Tweet","Sentiment"])
# 	writer.writeheader()

consumer_key = 'Your_key'
consumer_secret = 'Your_Secret'

access_token = 'Your_Access_token'
access_token_secret = 'Your_Access_secret'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

#Tweets
public_tweets = api.search('trump')

for tweet in public_tweets:
	l = []
	l.append(tweet.text)
	analysis = TextBlob(tweet.text)
	if analysis.sentiment.polarity > 0:
		a = "Positive"
	elif analysis.sentiment.polarity < 0:
		a = "Negative"
	else:
		a = "Neutral"
	l.append(a)
	with open('tweets.csv','a') as outcsv:
		writer = csv.writer(outcsv)
writer.writerow(l)