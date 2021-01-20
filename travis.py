#Travis, the ridiculous security robot

known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]
print(len(known_users))

while True:
    print("Hi! My name is Travis.")
    name = input("What's your name? ").strip().capitalize()

    if name in known_users:
        print("Wah's poppin {}?!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").lower()

        if remove == "y":
            known_users.remove(name)
            print ("peace")
        elif remove == "n":
            print("Dope.")
            
    else:
        print("Hmmmm...sus af {}...".format(name))
        add_me = input("Squad up? (y/n)?: ").strip().lower()

        if add_me == "y":
            known_users.append(name)
            print("Welcome to the squad {}!".format(name))
        elif add_me == "n":
            print("Fuq outta here, {}, ya bish".format(name))
