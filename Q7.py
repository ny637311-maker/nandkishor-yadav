
students = {"Aman", "Riya", "Sohan", "Riya", "Aman", "Neha"}

print("Students set:", students)


students.add("Karan")
students.add("Priya")
print("After adding new students:", students)


marks = {
    "Aman": 82,
    "Riya": 67,
    "Sohan": 55,
    "Neha": 74
}


for student, score in marks.items():
    if score >= 75:
        result = "Distinction"
    elif score >= 60:
        result = "Pass"
    else:
        result = "Fail"
    
    print(student, ":", score, "-", result)