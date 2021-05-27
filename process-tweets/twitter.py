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
  tweetId = originalTweet["id_str"]
  screenName = originalTweet["user"]["screen_name"]
  print('Replying to', tweetId)
  # api.update_status(f"@{screenName} {text}", tweetId)
  try:
    api.update_status(status = text, in_reply_to_status_id = tweetId , auto_populate_reply_metadata=True)
  except tweepy.TweepError as e:
    print("Error", e)
    message = e[0]["message"]
    errorTweetText = f"Whoops, we encountered an error! Message: {message}"
    api.update_status(status = errorTweetText, in_reply_to_status_id = tweetId , auto_populate_reply_metadata=True)
  except:
    print("Unknown error")
    errorTweetText = f"Whoops, we encountered an unknown error!"
    api.update_status(status = errorTweetText, in_reply_to_status_id = tweetId , auto_populate_reply_metadata=True)
