#Given a list of numbers, find the largest number in the list
num_list = [1, 2, 3, 17, 5, 9, 13, 12, 11, 4]

highest = num_list[0]
for number in num_list:
    if number > highest:
        highest = number

print(highest)