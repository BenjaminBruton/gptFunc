import json

with open('config.json') as config_file:
    config = json.load(config_file)

secret_key = config['SECRET_KEY']
prompt = 'Give me an outline for a course on how to make web applications using Bubble'

import openai
openai.api_key = secret_key

output = openai.Completion.create(
    model='text-davinci-003',
    prompt=prompt,
    max_tokens=300,
    temperature=0
)

output_text = output['choices'][0]['text']
print(output_text)