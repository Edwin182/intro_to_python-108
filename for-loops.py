"""
A for loop in python is a control structure that lets you repeat a block of code for each item in a sequence (such as list, string, tuple, range of numbers...)

It's used when you know how many times you want to repeat an action or when you want to process each element in a collection. 

for variable in sequence: 
    # code block runs each item in the sequence
"""

# loop through a list 
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:            # for each fruit (item) in the list fruits
    print(fruit)

# loop through a string
for letter in "hello":
    print(letter)

print("-----------------------------------")

# range() generates a sequence of numbers 
for x in range(5):
    print(x)

print("-----------------------------------")

# START and END range
for x in range(2, 6):
    print (x)

print("-----------------------------------")

# START, STOP, STEP
for x in range(0, 10, 2):       # start at 0, end at index 10, skip by 2
    print(x)

print("-----------------------------------")

# ELSE in for loop
for x in range(3):
    print(x)
else:                           # else always runs after the loop
    print("loop is done")

print("-----------------------------------")

# BREAK and CONTINUE in for loops
for x in range(10):
    if x== 5:
        continue            # skips 5 and continues to the next
    if x== 8:
        break               # Stops the loop completely 
    print(x)

print("-----------------------------------")

# ENUMERATE() - get the index and the value
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

print("-----------------------------------")

# you can even choose where the counbting starts 
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

print("-----------------------------------")

# ZIP()  - loop through two list together 
# zip() pairs up items from multiple sequences by position, 
# so you can loop through them side by side

names = ["Leo", "Alex", "Smith"]
scores = [92, 85, 78]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

print("-----------------------------------")

# NESTED for loops (a loop inside a loop)
for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row}, {col})", end=" ")
    print()         # move to a new line after each row finishes. 


"""
MINI-CHALLENGE
1. Ask the user to enter a number and store it in a variable called num.
3. Use a for loop with range(1, 11) to repeat 10 times (from 1 to 10)
3. inside the loop, multiply num by the current loop value (i)
"""

num = int(input("Enter a number: "))

""" this is one way to do it
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
"""

num = int(input("Enter a number: "))
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")