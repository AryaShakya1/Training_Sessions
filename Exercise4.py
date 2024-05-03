list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

#Case having empty lists
# list1 = []
# list2 = []


concatenated_list = []
for first_index in range(len(list1)):
    for second_index in range(len(list2)):
        concatenated_list.append(str(list1[first_index]) + str(list2[second_index]))


print(concatenated_list)
