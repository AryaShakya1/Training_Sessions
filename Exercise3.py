# numbers = [1, 2, 3, 4, 5, 6, 7]#Normal case


# numbers=[] #Empty list

numbers = ["1", 2, 3, "4", 5, 6, 7]


squares = []
for number in numbers:
    squares.append(int(number) * int(number))

print(squares)
