import twitter
import gpt3
import re

def main(event, context):
    print(event)
    for newTweet in event:
        rawText = newTweet['text']
        ourName = "@SmartBotAI"
        removeOurNameRegex = re.compile(re.escape(ourName), re.IGNORECASE)
        text = removeOurNameRegex.sub('', rawText)
        print('Processing', text)

        response = gpt3.getResponse(text)

        print('Tweeting', response)

        twitter.replyToTweet(newTweet, response)

    return True
