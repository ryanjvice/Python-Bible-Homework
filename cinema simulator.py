films = {
    "Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghostbusters": [12,5]
    }

while True:
    choice = input("What movie would you like to see? ").strip().title()
    
    if choice in films:
        age = int(input("How old are you? ").strip())

        #check user age
        
        if age >= films[choice][0]:
            #check enough seats

            num_seats = films[choice][1]

            if num_seats>0:
                print("Enjoy")
                films[choice][1] = films[choice][1] -1
            else:
                print("Sorry, sold out.")
        else:
            print("Too young.")
            
    else:
        print("We don't have that film...")


while True:
    choice
