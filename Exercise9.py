"""
Exercise 9: Replace list item with new value if found

"""

list1 = [5, 10, 15, 20, 25, 50, 20]

target = 20
value = 200
index = 0

try:
    index = list1.index(target)
except ValueError:
    print("Not found")

list1[index] = value
print(list1)
