films = {
    "Laserface":[13,1],
    "Gatcha":[7,1],
    "Home":[7,1]
    }

while True:

    choice = input("What would you like to see today?: ").strip().title()
    if choice in films:

        num_tix = films[choice][1]
        if num_tix > 0:

            age = int(input("How old are you?: "))
            if age >= films[choice][0]:

                print("Enjoy the show!")
                films[choice][1] = films[choice][1] - 1

            else:
                print("Sorry, you aren't old enough for that film.")

        else:
            print("Sorry, we are sold out for that showing.")
        
    else:
        print("Sorry, we aren't showing that today.")
