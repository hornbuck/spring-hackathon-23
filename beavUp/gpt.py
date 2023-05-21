import os
import openai
import requests

openai.api_key = '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'


# FUNCTION: NPC Dialogue Generation
# INPUTS: Type, Name, Personality Attributes
# OUTPUTS: AI-Generated Phrase
def dialogue(npc, name, personality):
    result = ""

    # Generates a prompt
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user",
             "content": "You are " + str(name) + ", a " + str(personality) + str(npc) + "that gives directions to the "
                                                                                        "top of the of the mountain to our protagonist, Beavy. Output some text of 20 words or less "
                                                                                        "telling him to go to the top of the mountain, remember your personality!"}
        ]
    )

    # Parses response
    response = completion.choices[0].message
    result = response["content"]

    return result


# FUNCTION: Image Generation
# INPUTS: Prompt, preferred path of image
# OUTPUTS: None - void
def newImage(subject, path):
    response = openai.Image.create(
        prompt=str(subject),
        n=1,
        size="1024x1024"
    )

    image_url = response['data'][0]['url']

    data = requests.get(image_url).content

    f = open(path, "wb")

    f.write(data)
