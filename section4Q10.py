students = {
    "Rahul": {"age": 20, "marks": 85},
    "Priya": {"age": 21, "marks": 90},
    "Rohan": {"age": 19, "marks": 75}
}


students["Amit"] = {"age": 22, "marks": 80}


students["Rahul"]["marks"] = 95

del students["Rohan"]

print("Is Priya present?", "Priya" in students)  

for name, details in students.items():
    print(f"Name: {name}, Age: {details['age']}, Marks: {details['marks']}")