translate = input("What would you like to translate?: ").strip().lower()

words = translate.split()

new_words = []

for word in words:

    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)

    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        rest = word [vowel_pos:]
        new_word = rest + cons + "ay"
        new_words.append(new_word)

output = " ".join(new_words)
print (output)
