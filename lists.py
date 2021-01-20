our_list2 = [1, 2, 3, (4, 5, 6), 7, 8, 9]
print(our_list2[0:3])
print(our_list2[3])
print(our_list2[3][0])
print(our_list2[3][1])
print(our_list2[3][2])
print(our_list2[4:7])
print(our_list2)

if our_list2[1] == 1:
    print("yes")
elif our_list2[1] == 3:
    print("yes")
else:
    print ("nope")
    
A = our_list2[0]
B = our_list2[2]
C = our_list2[1]

string = "One {} three {} two {}"
output = string.format (A, B, C)
print(output)

our_list2 = [1, 2, 3, ((4, 5, 6), 7, 8, 9, input("Number: "))]
print(our_list2)

a_table =[(1,2,3),(4,5,6),(7,8,9)]
print(a_table[0])
print (a_table[1])
print (a_table[2])
print (a_table[0][1])

