
def multiply (x,y):
    return x*y

answer = multiply(5,10)
print(answer)



def rev(text):
    return text[::-1]

answer = input("flip it!: ").strip().lower()
flip = rev(answer)
print(flip)

again = flip[::-1]
print(again)
