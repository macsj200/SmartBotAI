import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
prompt = "Harry Dresden, Chicago's only"
response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=50)
print(prompt + response['choices'][0]['text'])
