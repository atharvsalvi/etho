from dotenv import load_dotenv
import base64
import os
from google import genai
from google.genai import types

load_dotenv()

def generate(user_input):
    client = genai.Client(
        api_key = os.environ["GEMINI_API_KEY"]
    )

    model = "gemini-2.5-pro"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""Create a new folder named Test"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""**Clarifying the Goal**

I'm focusing on understanding the user's desire to establish a new directory named \"Test.\" Initially, this meant understanding it as a directory-building operation. Now, it's about connecting that intent to the tools needed. I'm exploring the PowerShell commands, especially `mkdir`, which seems the direct fit.


**Analyzing Command Structure**

Now I'm diving deeper into the nuances of `mkdir \"Test\"`. It's clear `mkdir` maps to `New-Item -ItemType Directory`.  I'm focusing on why  `\"Test\"` works as the positional parameter for the `-Path` argument. My goal now is to solidify my understanding of parameter binding in PowerShell and how aliases function to determine what arguments are provided.


**Confirming Command Selection**

I've solidified my choice, landing on `mkdir Test`. It directly addresses the user's need, using the most common PowerShell method. I considered the nuances of `New-Item` and the aliases, ultimately favoring brevity and familiarity. The format will be a simple command output, as requested.


"""),
                types.Part.from_text(text="""mkdir Test"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""add this repo to git, all files"""),
            ],
        ),
    ]
    tools = [
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1,
        ),
        tools=tools,
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""
            You are a terminal agent and your name is Etho. You take input from users and convert them into powershell commands and execute them immediately. Make sure you don't include any additional response or markdowns. If the user tries to have a friendly conversation then reply in the same tone.
            if the user is giving order to do something on terminal, then add 'Order!@#$%^&*()' at the very start and the command on next line.
            """),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()

