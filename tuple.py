"""
Tuples are just like lists- BUT!!! thay are IMMUTABLE (can't change after creating)
Created with () 
"""

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# accessing items
print(my_tuple[1])
print(my_tuple[-2])

# check if item exists
if "apple" in my_tuple:
    print("Yes")

# length of a tuple
print(len(my_tuple))

# single item tuple
# You must add a comma at the end or python wont recogniz it as a tuple
single = ("water",)
print(type(single))
not_tuple = ("water")
print(type(not_tuple))


# nested tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
combined = (tuple1, tuple2)
print(combined)

# Count and Index
# Because tuples are immutable, they dont have methonds like remove or add
letters = ("a", "b", "a", "c", "a")
print(letters.count("a"))  # how many times "a" appears
print(letters.index("c"))  # the index where "c" first appears

# Tuple Unpacking
# You can "unpack" a tuple's items directly into separate variables.
coordinates = (10, 20)
x, y = coordinates
print(x)
print(y)

person = ("leo", 27, "Computer science")
name, age, major = person
print(f"{name} is {age} years old and studies {major}")


# -------------------------------
#  MINI CHALLENGE: THE TRAVEL BAG
# -------------------------------
# You’re packing for a trip! You have a tuple that stores the items you’re taking.

# 1. Create a tuple called "travel_bag" with at least 5 items (e.g. "shirt", "toothbrush", etc.)
# 2. Print the SECOND and FOURTH items in your bag.
# 3. Check if "shoes" is in your travel bag — if it is, print "You're ready to walk!"
#     otherwise, print "You forgot your shoes!"
# 4. Make a new tuple called "essentials" with 3 must-have items.
# 5. Combine both tuples into one called "final_bag".
# 6. Print how many total items you now have using len().
# 7. Print the last item in your "final_bag".














