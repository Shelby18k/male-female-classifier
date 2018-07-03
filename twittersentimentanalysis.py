import tweepy
from textblob import TextBlob
import csv

# with open('tweets.csv','wt') as outcsv:
# 	writer = csv.DictWriter(outcsv,fieldnames=["Tweet","Sentiment"])
# 	writer.writeheader()

consumer_key = 'Jo9NR2J8QaRFYVpjmcskhXmYA'
consumer_secret = 'ok9aASYXWvIECWtfC17fcPz6XUVukqfO0XjwQpXAY6r3wT0amb'

access_token = '327371942-eDzP6scpgS79iCU20Mym8ixPXNvXhRZL3NO3SqNR'
access_token_secret = '9Hm7oZvls0TSzVArHfG5gL6F2uwCbXgPAE1BVnztGAlfc'

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
	