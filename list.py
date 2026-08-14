"""
List store multiple items in a single variable
List are created usin g = []
"""

mylist = [10, 20, 30, 40, 50]
print(mylist)

# Can contain different data types 
mixedlist = [1, "apple", 3.5, True]
print(mixedlist)

# Accessing items by INDEX
# indexing starts at 0

fruits = ["apple", "banana", "cherry"]
print(fruits [1])
print(fruits [0])

# You can use NEGATIVE indexes to count from the END
print(fruits[-1])
print(fruits [-3])

# Modifying List items
fruits[1] = "mango" # changes banana to mango
print(fruits)

# Adding item to the. list (only works one item at a time)
fruits.append("orange") # adds one item to the END of the list 
print(fruits)

fruits.insert(1, "kiwi") # adds before the index (in this case after index 1)
print(fruits)

fruits.extend(["grape", "pear"]) # adds MULTIPLE items to the end of the list
print(fruits)

# Removing Items
fruits.remove("apple") # removes by exact VALUE (the first match it finds)
print(fruits)

fruits.pop() # removes the LAST item on the list (you can also use (index) and it will remove specific index)
print(fruits)

#fruits.clear() # Deletes the whole list leaving it empty []
#print(fruits)

# Looping through a list 
for x in fruits:
    print (x)

# Checks if item exist 
if "mango" in fruits:
    print("yes mango is in the list")

# List lenght
print(len(fruits)) # Number of items in list 

# Slicing a list 
# Slicing lets you grab a RANGE of items using [start:stop:step]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5]) #[2:5] means a range between 2 to 5 (index 2- 5)
print(numbers[:4])  # start from the very beginning up to index 4
print(numbers[6:])  # starts at index 6 until the end of the list 
print(numbers[-3:]) # returns the last 3 items 
print(numbers[::2]) #step skips every 2nd item 

# useful list methods 
numbers = [4, 2, 9, 1, 7]

print(numbers.count(2))     # counts number of times the item is in the list 
print(numbers.index(9))     # returns the index where the first appears

numbers.sort(reverse=True)          # Sorts the list in place from smallest to largest (remove reverse = true and it will do it, keep it and it will fdo from largest to smallest)
print(numbers)

numbers.reverse()       # flips current order of the list
print(numbers)

number_copy = numbers.copy()    #makes a REAL copy of the list
print(number_copy)

# -------------------------------
#  MINI CHALLENGE: THE GROCERY LIST
# -------------------------------
# You're building a grocery list app.
# 1. Create a list called "groceries" with at least 5 items.
# 2. Print the first and last item using indexing.
# 3. Use slicing to print just the first 3 items.
# 4. Add "eggs" to the end of the list using append().
# 5. Insert "milk" at the very beginning of the list.
# 6. Remove one item using remove().
# 7. Check if "bread" is in the list — print a message either way.
# 8. Sort the list alphabetically and print it.
# 9. Print how many items are in the final list.

# 1. Create a list called groceries with at least 5 items
groceries = ["bread", "rice", "chicken", "apples", "cheese"]
print(groceries)

# 2. Print the first and last item using indexing
print(groceries[0])   # First item
print(groceries[4])  # Last item

# 3. Use slicing to print just the first 3 items
print(groceries[:3])

# 4. Add "eggs" to the end of the list using append()
groceries.append("eggs")
print(groceries)

# 5. Insert "milk" at the very beginning of the list
groceries.insert(0, "milk")
print(groceries)

# 6. Remove one item using remove()
groceries.remove("rice")
print(groceries)

# 7. Check if "bread" is in the list
if "bread" in groceries:
    print("Yes, bread is in the grocery list.")
else:
    print("No, bread is not in the grocery list.")

# 8. Sort the list alphabetically and print it
groceries.sort()
print(groceries)

# 9. Print how many items are in the final list
print(len(groceries))