# Case having same number of elements in both lists
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

# Case having lists of different size
list1 = [10, 20, 30, 40, 50, 60]
list2 = [100, 200, 300, 400]

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400, 500, 600]

# Case having empty lists
list1 = []
list2 = []


reversed_list2 = list2[::-1]
min_length = min(len(list1), len(list2))

for index in range(min_length):
    print(list1[index], reversed_list2[index])

if len(list1) > len(list2):
    for index in range(min_length, len(list1)):
        print(list1[index])
elif len(list1) < len(list2):
    for index in range(min_length, len(list2)):
        print(reversed_list2[index])
