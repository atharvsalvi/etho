from gemini import generate
import os

session = True
while(session) :
    userInput = input(">> ")
    if(userInput == "exit"): break
    texts = generate(userInput).split('\n')
    for text in texts :
        os.system(text)