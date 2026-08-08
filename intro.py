print("Hello World from python!")
print(2)
print(5+3)
print(True)

# SHORCUTS:
# save file: cmd + S
# up on arrow key goes to the previous commands 

"""
multi line. Make sure to use 3 quotes before and after
these comments will be ignored by python. these are comments for me
"""

#Variables and Concatenation
name = "Edwin"
age = 45
print(name, age)

print("my name is " + name + " and I am " + str(age) + " years old." )

'''
minichallenge 
Write a short story using variables. 
1. Declare and initialize 5 variables (strings and numbers)
2. use print() and concatenation to tell a story
3. run the program in terminal
'''


name = "Edwin"
age = 45
served_years = 22
retire_date = "December 4, 2026"
branch_served = "Navy"

""" print(" my name is "+ name + " I am " + str(age) + " years old " + " I served in the military for " + str(served_years) + " I will retire on " + retire_date + " I served in the " + branch_served)"""

print(f"My name is {name}, I am {age} years old. I served in the military for {served_years} years and I will retire on {retire_date} I served in the {branch_served} ")

#Type Function 
print(type(name)) # string
print(type(age)) # int
print(type(False)) # boolean

# Casting (changing data types)
print(20 + int("20"))

# User Input Function 
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}!")

# input() always returns a string
print(type(input("enter your name: ")))

new_age = int(input("Enter your age: "))
print(age + new_age)

"""Pizza Calculator
1. Ask how many slices of pizza and how many people.
2. Use math operators to calculate slices per person. (divide /)
3. Show the results with an f-string
"""

pizza_slices = int(input("How many slices of pizza do you want? "))
people = int(input("How many people are sharing the pizza? "))

slices_per_person = pizza_slices / people

print(f"Each person gets {slices_per_person} slices of pizza.")



