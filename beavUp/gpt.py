import os
import openai
openai.api_key = '*'

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "You are Bob, a shy and cryptic cougar that gives directions to the top of the of the "
                                "mountain to our protagonist, Beavy. Output some text of 20 words or less telling him "
                                "to go to the top of the mountain, remember your personality!"}
  ]
)

print(completion.choices[0].message)
