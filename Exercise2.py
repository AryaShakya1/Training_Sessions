list1 = [1, "na", "i", "Ke","H"]
list2 = ["y", "me", "s", "lly","i"]

min_length = min(len(list1),len(list2))
ans=[]
for index in range(min_length):
    ans.append(list1[index]+list2[index])

if len(list1) > len(list2):
    for index in range(min_length,len(list1)):
        ans.append(list1[index])
elif len(list1) < len(list2):
    for index in range(min_length,len(list2)):
        ans.append(list2[index])

print(ans)
