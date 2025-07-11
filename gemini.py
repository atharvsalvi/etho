from dotenv import load_dotenv
import base64
import os
from google import genai
from google.genai import types

load_dotenv()

def generate():
    client = genai.Client(
        api_key = os.environ["GEMINI_API_KEY"]
    )
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents=" add and commit to git with message add and commit from the code itself",
        config=types.GenerateContentConfig(
            system_instruction = "Give the response in the form of powershell commands only. Do not add any additional content or markdown."
        ),
    )
    return response.text