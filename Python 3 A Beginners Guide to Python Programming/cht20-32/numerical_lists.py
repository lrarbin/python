# 15/05/2021
# Laurence Arbin
# The range function

# using the range function

for value in range(1,5):
    print(value)


# Creating a list of numbers
# Converting numbers into a list

numbers = list(range(1,6))

print(numbers)

odd_numbers = list(range(1,101,2))

print(odd_numbers)

squares =[]

for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

digits = [1, 2, 3, 4, 5]

print(min(digits))

print(max(digits))

print(sum(digits))