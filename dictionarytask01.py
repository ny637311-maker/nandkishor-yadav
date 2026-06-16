# Create dictionary
students = {
    "Rahul": 85,
    "Priya": 90,
    "Rohan": 65
}

# Loop and check marks
for name, marks in students.items():
    if marks > 75:
        print(f"{name} - Pass")
    else:
        print(f"{name} - Fail")







