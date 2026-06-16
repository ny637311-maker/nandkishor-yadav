
cities = ["Delhi", "Mumbai", "Chennai", "Kolkata", "Bangalore", "Hyderabad", "Pune", "Ahmedabad"]


print("First 4 cities:", cities[:4])


print("Last 4 cities:", cities[-4:])


cities.append("Jaipur")
print("After adding a city:", cities)


cities.pop(0)
print("After removing first city:", cities)


cities_tuple = tuple(cities)
print("Tuple:", cities_tuple)