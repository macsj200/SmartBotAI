import tweepy
import os

consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")

access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# @SmartBo69928874 -filter:replies
api.update_status("Bleep Bloop 🤖")
