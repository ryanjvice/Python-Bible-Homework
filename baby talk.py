#generate random question
#allow person to attempt an answer
#as long as answer isn't "just because," keep asking, "but why?"
#once "just because" is answered, ask another question, forever

while True:

    from random import choice

    question = ["Why is the sky blue?: ", "Why don't the stars fall?: ", "Where does the sun go?: ".strip().lower()]
    answer = input(choice(question))
    
    while answer != "just because".strip().lower():
        answer = input("...but why? ")
