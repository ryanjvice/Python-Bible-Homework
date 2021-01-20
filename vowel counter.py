word = "supercalifragilisticexpialidocious"
vowels = 0
consonants = 0

for letter in word:
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == " ":
        pass
    else:
        consonants = consonants + 1

print(word)
print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))



