#SET OPERATIONS 

set1 = {"Python", "Java", "C++", "Python", "JavaScript", "C++"}
print("Set (unique values):", set1)


set2 = {"Python", "C", "Java"}


print("Union:", set1 | set2)


print("Intersection:", set1 & set2)


print("Difference:", set1 - set2)


# ----- TUPLE OPERATIONS -----


cities = ("Indore", "Bhopal", "Delhi", "Mumbai", "Indore")

print("Count of Indore:", cities.count("Indore"))


print("Index of Delhi:", cities.index("Delhi"))

print("Is Pune present?", "Pune" in cities)


try:
    cities[0] = "Pune"
except TypeError:
    print("Error: Tuple cannot be modified (immutable)")