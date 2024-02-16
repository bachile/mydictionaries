student = {"name": "Brando",
           "age": 21,
           "major": "MIS",
           "hobbies": ["guitar", "tennis", "reading"]}

student["State"] = "Texas"

student["age"] += 1

for info in student:
    print(f'{info}: {student[info]}')