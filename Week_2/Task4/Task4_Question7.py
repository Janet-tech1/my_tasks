# List Manipulation
# Create a list of five cities.
cities = ["Abeokuta", "Sagamu", "Ikeja", "Epe", "Lekki"]
print(cities)
# Replace the third city with a new one (entered by the user).
cities[2] = "Agege"

# Remove the last city.
cities.remove("Lekki")

# Add a new city to the beginning of the list.
cities.insert(0, "Ota")

# Print the updated list.
print(cities)
