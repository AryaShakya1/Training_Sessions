# Exercise 7: Add new item to list after a specified item

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]


def find_index_in_nested_list(nested_list, target):
    def recurse(items, path):
        for index, item in enumerate(items):
            new_path = path + [index]
            if item == target:
                return new_path
            elif isinstance(item, list):
                result = recurse(item, new_path)
                if result is not None:
                    return result
        return None

    return recurse(nested_list, [])


index = find_index_in_nested_list(list1, 6000)
value = list1
for i in range(len(index) - 1):
    value = value[index[i]]

print(list1)
print(value)
value.append(7000)
print(value)
print(list1)
