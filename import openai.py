import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "hell "}])
print(completion.choices[0].message.content)