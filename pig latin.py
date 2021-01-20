#get sentence from user
#split sentence into words
#loop through words

#if word starts with vowel, add "yay"
#if word starts with consonants, add "ay"

#convert into pig latin
#stick words back together
#output final string


translate = input("What would you like to translate?: ").strip().lower()

words = translate.split()

new_words= []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos +1
            else:
                break
        cons = word[:vowel_pos]
        word_rest = word[vowel_pos:]
        new_word = word_rest + cons + "ay"
        new_words.append(new_word)

output = " ".join(new_words)
print(output)
