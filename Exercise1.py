list1 = [100, 200, 300, 400, 500]


# Empty list
# list1 = []

reversed_list = list1[::-1]

reversed_list = []
length = len(list1)
for index in range(length):
    reversed_list.append(list1[(length - 1) - index])

print(reversed_list)
