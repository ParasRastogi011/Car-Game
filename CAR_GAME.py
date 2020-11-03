# Car-Game
Intro = """Now, Lets Begin! 
-New Players, 
-ENTER >  Help"""
print(Intro)
Command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("Car started...")
    elif command == "stop":
        print("Car stopped...")
    elif command == "help":
        print("""start - to start the car\nstop - to stop the car\nquit - to quit""")
    elif command == "quit":
        break
    else:
        print("I don't understand...")

