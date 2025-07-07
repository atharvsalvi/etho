
print("Hello, this is your bot Etho.")
print("May I know your name?")
name = input("Name >> ")
print(f"Welcome, {name}! How may I help you?")
while(True) :
    interaction = input(">> ")
    if interaction == "exit" :
        print(f"Goodbye {name}! Remember, always type 'etho' in your powershell and I will be at your service!")
        break