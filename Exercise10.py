# Exercise 10: Remove all occurrences of a specific item from a list.

list1 = [5, 20, 15, 20, 25, 50, 20]

# Empty list
list1 = []

# Item to be removed
target = 20

while target in list1:
    list1.remove(target)

print(list1)
