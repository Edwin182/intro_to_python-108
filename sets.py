"""
Sets are UNORDERED, UNINDEXED, and have NO DUPLICATES
Created with {}
"""


fruits = {"apple", "banana", "cherry"}
print(fruits)


# NO DUPLICATES ALLOWED
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)


# check if item exists
print("bananna" in fruits)


# Adding items
fruits.add("orange")
print(fruits)


# adding multiple items
fruits.update(["kiwi", "mango"])
print(fruits)


# Remove items
fruits.remove("banana")
print(fruits)


# If you're not sure an item exists, use discard() to avoid errors
fruits.discard("water")
print(fruits)


# Set Operations (like in math)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))                    # combine both (with no duplicates)
print(set1.intersection(set2))             # common elements (duplicates)
print(set1.difference(set2))               # whats unique in set 1
print(set1.symmetric_difference(set2))     # everything except duplicates

"""
-------------------------------
MINI CHALLENGE: STUDY GROUPS
-------------------------------
Two study groups are preparing for an exam.
1. Create two sets:
    - group_a = {"Leo", "Sam", "Alex", "Nina"}
    - group_b = {"Nina", "Jordan", "Sam", "Taylor"}
2. Print:
    - All students participating in either group (union)
    - Students who are in BOTH groups (intersection)
    - Students who are only in group_a (difference)
3. Add "Maya" to group_a.
4. Remove "Jordan" from group_b.
5. Print the total number of unique students across both groups.
6. If "Nina" is in both groups,
        print("Nina is helping both groups!")
    Otherwise,
        print("Nina is only in one group.")
7. Print the final version of both sets.
"""

# 1. Create two sets with the students in each study group
group_a = {"Leo", "Sam", "Alex", "Nina"}
group_b = {"Nina", "Jordan", "Sam", "Taylor"}


# 2. UNION: Combine both groups and show every unique student
# If a student appears in both groups, they will only appear once
print(group_a.union(group_b))

# INTERSECTION: Show students who are in BOTH groups
# Sam and Nina are members of group_a AND group_b
print(group_a.intersection(group_b))

# DIFFERENCE: Show students who are in group_a but NOT in group_b
# Leo and Alex are only in group_a
print(group_a.difference(group_b))

# 3. Add Maya to group_a
# .add() adds one new item to a set
group_a.add("Maya")
print(group_a)

# 4. Remove Jordan from group_b
# .remove() removes the specified item from the set
group_b.remove("Jordan")
print(group_b)

# 5. Combine the groups and count the total number of unique students
# union() combines them without duplicates
# len() counts how many students are in the combined set
print(len(group_a.union(group_b)))

# 6. Check if Nina exists in BOTH groups
# "and" means BOTH conditions must be True
if "Nina" in group_a and "Nina" in group_b:
    print("Nina is helping both groups!")
else:
    print("Nina is only in one group.")

# 7. Print the final version of both groups
print(group_a)
print(group_b)