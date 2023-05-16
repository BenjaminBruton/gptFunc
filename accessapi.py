secret_key = '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'
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