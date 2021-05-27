import tweepy
import os

consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")

access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# @SmartBotAI -(from:SmartBotAI)
def replyToTweet(originalTweet, text):
  tweetId = originalTweet["id"]
  screenName = originalTweet["user"]["screen_name"]
  print('Replying to', tweetId)
  # api.update_status(f"@{screenName} {text}", tweetId)
  api.update_status(status = text, in_reply_to_status_id = tweetId , auto_populate_reply_metadata=True)

