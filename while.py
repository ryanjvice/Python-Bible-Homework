number = 1

while number <= 10:
    print(number)
    number = number + 1

while number <=100:
    if number % 2 != 0:
        print (number)
    number = number + 1
    
L = []

while len(L) < 3:
    new_name = input("Please add a new name: ").strip().capitalize()
    L.append(new_name)

print("Sorry list is full")
print(L)
