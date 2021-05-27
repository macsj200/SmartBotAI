import twitter
import gpt3

def main(event, context):
    print(event)
    for newTweet in event:
        text = newTweet['text']
        print('Processing', text)

        response = gpt3.getResponse(text)

        print('Tweeting', response)

        twitter.writeTweet(response)

    return True
