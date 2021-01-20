known_users = ["Alice","Bob","Charlie","Dan","Evan","Fairuka"]

while True:
    print("Hi! My name is Travis.")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system? )y/n): ").strip().lower()

        if remove =="y":
            known_users.remove(name)
            print ("Smell ya later, {}!".format(name))
        elif remove =="n":
            print("No problemo {}!".format(name))
            
    else:
        print("Hmm...I don't think we've met yet, {}!".format(name))
        add_me = input("Would you like to be added to the system? (y/n): ").strip().lower()
        if add_me == "y":
            known_users.append(name)
            print ("Welcome aboard, {}!".format(name))
        elif add_me == "n":
            print("No worries, catch you on the flippity flop.")
                
