a = 250

def f1():
    global a
    a = 100
    print(a)

def f2():
    b = a + 50
    print (b)

f1()
f2()
print(a)








		
