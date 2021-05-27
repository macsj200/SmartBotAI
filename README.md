# @SmartBotAI

## About

[@SmartBotAI](https://twitter.com/SmartBotAI) is an [OpenAI API](https://beta.openai.com/)-powered [GPT-3](https://en.wikipedia.org/wiki/GPT-3) Twitter bot. It will reply to tweets with a short prompt that mention @SmartBotAI with an "autocompleted" (AI-generated) follow up to the prompt.

Created by [@macsj200](https://twitter.com/macsj200) [github source](https://github.com/macsj200/gpt3)

### Examples

[Original tweet](https://twitter.com/macsj200/status/1397846950658052097):

```
@SmartBotAI complete the following function which computes the nth Fibonacci number in JavaScript:

function fib(n) {
```

[Autocompleted reply](https://twitter.com/SmartBotAI/status/1397847181621616644):

```
complete the following function which computes the nth Fibonacci number in JavaScript:

function fib(n) { var prev = 0; var curr = 1; var result; while (n-- > 0) { result = curr; curr = prev + curr; prev = curr; } return result; }

Also take a
```

Original tweet:

```
@SmartBotAI Harry Dresden, Chicago's only professional wizard hit the battlefield
```

Autocompleted reply:

```
Harry Dresden, Chicago's only professional wizard hit the battlefield. Well everything human, demonic and ordinarily foul goes around in threes.

RAW: So when Thomas and one of Mab's mercs made me, I hit the streets to hunt down the demon. Killed it
```

## How it works

The Twitter bot is all built on top of AWS Lambda. It uses [Tweepy](https://www.tweepy.org/) to programatically create tweets. It calls the OpenAI API to automatically generate text based on a prompt using the `openai` [Python library](https://github.com/openai/openai-python).

It uses `AWS Serverless Tweet Event Source` ([github link](https://github.com/wweiss/aws-serverless-tweet-event-source)) to poll a Twitter search query to get the set of new tweets that mention @SmartBotAI. This polling function runs once every 5 minutes.

When a new tweet is picked up the polling function invokes a [Serverless](https://www.serverless.com/) lambda function that calls the `openai` API with the tweet's prompt and posts an autocompleted response.
