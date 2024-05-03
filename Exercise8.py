list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]


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

index = find_index_in_nested_list(list1, "g")
value = list1
for i in range(len(index) - 1):
    value = value[index[i]]

print(list1)
print(value)
value.extend(sub_list)
print(value)
print(list1)
