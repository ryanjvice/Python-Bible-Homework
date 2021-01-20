students = {
    "male": ["Tom", "Charlie", "Harry", "Frank"],
    "female": ["Sara", "Emily", "Lucie"]
    }

for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)
