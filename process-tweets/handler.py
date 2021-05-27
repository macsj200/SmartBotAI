import twitter
import gpt3

def hello(event, context):
    for newTweet in event:
        print('Processing', newTweet.text)

        response = gpt3.getResponse(newTweet.text)

        print('Tweeting', response)

        twitter.writeTweet(response)

    return True
