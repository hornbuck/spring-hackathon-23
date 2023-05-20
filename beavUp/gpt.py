import os
import openai
openai.api_key = '*'

#FUNCTION: NPC Dialogue Generation
#INPUTS: Type, Name, Personality Attributes
#OUTPUTS: AI-Generated Phrase
def dialogue(npc, name, personality):

    result = ""

    #Generates a prompt
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": "You are " + str(name) + ", a " + str(personality) + str(npc) + "that gives directions to the "
                                    "top of the of the mountain to our protagonist, Beavy. Output some text of 20 words or less "
                                    "telling him to go to the top of the mountain, remember your personality!"}
      ]
    )

    #Parses response
    response = completion.choices[0].message
    result = response["content"]

    return result
    

#FUNCTION: Image Generation
#INPUTS: Prompt
#OUTPUTS: URL
def newImage(subject):

    response = openai.Image.create(
      prompt=str(subject),
      n=1,
      size="1024x1024"
    )

    return response['data'][0]['url']

#gen_image = newImage("mountain in Oregon")
#print(gen_image)
