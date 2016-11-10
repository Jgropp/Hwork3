# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.
import tweepy
from textblob import TextBlob

consumer_key = 'K8TBYVBBnz5IDUHQCv5iQRhiI'
consumer_secret = 'j8Y2BydLgNewQYN80z61ozzhafHhMaAeIBSKSnjYRBSPEz5Agg'
access_token = '796398976190844928-QTvOn7z0vzCBfrWyTx8dXkHHhpL8BYk'
access_token_secret = 'awAsuLWQwjZARUDf5Q9aO2L4Zv5UVzcLm9ZqQ9hc7C1qx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

search_term = input("Enter a term to search on twitter: ")
for tweet in tweepy.Cursor(api.search, q = search_term, result_type ='recent', include_entities = True,lang = 'en').items(100):
	print (tweet.text)

txt = TextBlob(tweet.text)
subj = txt.sentiment.subjectivity
pol = txt.sentiment.polarity
print("Average subjectivity is", subj)
print("Average polarity is", pol)