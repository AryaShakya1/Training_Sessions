list1 = [1, "na", "i", "Ke","H"]
list2 = ["y", "me", "s", "lly","i"]

min_length = min(len(list1),len(list2))
ans=[]
for i in range(min_length):
    ans.append(list1[i]+list2[i])

if len(list1) > len(list2):
    for i in range(min_length,len(list1)):
        ans.append(list1[i])
elif len(list1) < len(list2):
    for i in range(min_length,len(list2)):
        ans.append(list2[i])

print(ans)
