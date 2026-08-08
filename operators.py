# Arithmetic operators - used with numeric values to perform common math operations

x = 1
y = 2
res = 0

res = x + y
print(res)

res = x - y
print(res)

res = x * y
print(res)

res = x / y
print(res)

res = x % y # Modulus - removes the remainder after division
print(res)

res = x ** y # Exponentation x to the power of y 
print(res)

res = x // y # Floor division - divide and drop the decimal 
print(res)

# Asignment operator -  used to assign values to a variable 
# +=, -=, *=. /=

z = 5
z += 5
z -= 3
z *= 3
z /= 2
print(z)

# comparison operator - used to compare two values, same as if and else 
# == (equal to),  != (not equal), < > (greater than/less than) <= >= 

# Logical operator - used to combine conditional statements 
# used with True/False value like conditions
# # and -> both must be True
# # or -> at least one must be True
# not -> flips True to False (vice versa)

x = 3
y = 10
z = 10

print(x == y and z == x) # False, because both conditions are NOT True
print(x == y or y == z) # True, because at least one condition is True
print(not x == y) # True, because X not equal to y 

# Identity operator- used to compare the objects, not if the are equal but if they are actually the same object with the same memory location
# is -> check if two things are the smae
# is not -> check if they are not the same

x = 3
y = 3
print(x is y)  # Returns True if both variables are the same object
print(x is not y) #Returns True if both variables are NOT the same object 

# Membership Operator - used to test if a sequence is presented in an object 
# in -> checks if something exist inside a sequence(list, string, etc ...)
# not in -> checks if something does NOT exist inside a sequence(list, string, etc ...)

x = [1, 2, 3, 4, 5]

print(4 in x) # True because 4 is inside the list 
print(9 not in x) # True because 9 is not inside the list 

