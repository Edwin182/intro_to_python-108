'''
An if-else statement in pythin is a conditional control structure that lets you decide which block of code to run depending on whether a condition it True or False. 

The if block runs only if the condition evalueates to True.
- If - the condition is false , the else bloxk run instead
- You can also add elif (else if) block to check multiple conditions in a sequence 

if condition:
    - Code block runs if condition is True
elif another condition:
    -Code block runs if the first condition. is False
    -and this conitio is True
else:
    - Code block always runs if none of the above conditions are True
'''

x = 7

if x > 0:
    print("x is a positive number")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# Short Hand IF statements
if x > 5: print("x is greater than 5")

# Short hand IF... ELSE
print("Even") if x % 2 == 0 else print("Odd")

# Nested IF statements  (both conditions need to be true)
if x > 0:
    if x < 20:
        print("x is a positive number less than 20")

# Combining conditions
age = 19

if age >= 18 and age <=21:
    print("You are in between 18 and 21 years old")

"""
Mini challenge
Ask the user to enter a number from 0-100 and store it in a variable called "score".
If the score is 90 or above, print "Grade: A".
If the score is between 80-89, print "Grade: B".
If the score is between 70-79, print "Grade: C".
Otherwise, print "Grade: F".
6. Create a variable "passed" — set it to True if score >= 70, otherwise False.
BONUS: If passed is True, print "Congratulations!", otherwise print "Try again!"
"""

# Ask the user to enter a score
score = int(input("Enter a score from 0 to 100: "))

# Determine the letter grade
if score >= 90:
    print("Grade: A")
elif 80 <= score <= 89:
    print("Grade: B")
elif 70 <= score <= 79:
    print("Grade: C")
else:
    print("Grade: F")

# True if the score is 70 or higher; otherwise, False
passed = score >= 70

# Bonus
if passed:
    print("Congratulations!")
else:
    print("Try again!")
