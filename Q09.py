import json

try:
  
    students = [
        {"name": "Aman", "age": 20, "city": "Delhi", "course": "BCA", "marks": 75},
        {"name": "Riya", "age": 21, "city": "Mumbai", "course": "BBA", "marks": 68},
        {"name": "Sohan", "age": 19, "city": "Pune", "course": "BSc", "marks": 82},
        {"name": "Neha", "age": 22, "city": "Chennai", "course": "BA", "marks": 60}
    ]

    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

    
    with open("students.json", "r") as file:
        data = json.load(file)

   
    print("Students with marks > 70:\n")
    for student in data:
        if student["marks"] > 70:
            print(student)

    
    print("\nTotal number of students:", len(data))

except FileNotFoundError:
    print("File not found.")

except json.JSONDecodeError:
    print("Error decoding JSON.")

except Exception as e:
    print("An error occurred:", e)