from gemini import generate
import os

# print("Hello, this is your bot Etho.")
# print("May I know your name?")
# name = input("Name >> ")
# print(f"Welcome, {name}! How may I help you?")
# while(True) :
    # interaction = input(">> ")
texts = generate().split('\n')

for text in texts :
    os.system(text)