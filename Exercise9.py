list1 = [5, 10, 15, 20, 25, 50, 20]

target = 20
value = 200
ind = -1

for index in range(len(list1)):
    if list1[index] == target:
        ind = index
        break

if ind != -1:
    list1[ind] = value

print(list1)
