#Ask user for name

name = input("What is your name?: ")

#Ask user for age

age = int(input("What is your age?: "))

#Ask user for city

city = input("What city do you live in?: ")

#Ask user what they enjoy

enjoy = input("What do you enjoy?: ")

#Create output text

string = "Your name is {} and you are {} years old. You live in {} and you enjoy {}. :) "
output = string.format(name, age, city, enjoy)

#Print output to screen


start = "I am "
age = 20
end = " years old"
string = "{}{}{}"
output = string.format (start, age, end)
print (output)
