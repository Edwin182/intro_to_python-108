# =======================================
# PART 1: WORKING WITH A LIST
# =======================================

# Creating a new list
navy_locations = ["San Diego", "Hawaii", "Virginia", "Florida", "Japan"]
print(navy_locations)
print(len(navy_locations))


# Accessing items by index
print(navy_locations[0])
print(navy_locations[2])
print(navy_locations[-1])


# Replacing a value
navy_locations[3] = "Washington"
print(navy_locations)
print(len(navy_locations))


# Removing an item by value
navy_locations.remove("Virginia")
print(navy_locations)
print(len(navy_locations))


# Removing an item by index
navy_locations.pop(1)
print(navy_locations)
print(len(navy_locations))


# =======================================
# PART 2: WORKING WITH A DICTIONARY
# =======================================

# Creating a new dictionary
service_member = {
    "name": "Edwin",
    "branch": "Navy",
    "rank": "Chief",
    "years_of_service": 21
}

print(service_member)
print(len(service_member))


# Accessing values using keys
print(service_member["name"])
print(service_member["rank"])

# The dictionary has not changed
print(service_member)
print(len(service_member))


# Adding a new key
service_member["specialty"] = "Special Operator"
print(service_member)
print(len(service_member))


# Updating an existing value
service_member["years_of_service"] = 22
print(service_member)
print(len(service_member))


# Removing a key
service_member.pop("branch")
print(service_member)
print(len(service_member))