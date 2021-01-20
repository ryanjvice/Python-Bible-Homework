while True:
    from random import choice
    
    questions = ["Why is the sky blue?: ", "Why does the moon have a face on it?: ", "Where are all the dinosaurs?: "]

    question = choice(questions)
    answer = input(question).strip().lower()

    while answer != "just because".strip().lower():
        answer = input("...but, why?: ").strip().lower()
