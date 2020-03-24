list_of_big_numbers = []

for num in range(1500, 20001):
    #check if divisible by 5 and 7
    if num % 5 == 0 and num % 7 == 0:
        list_of_big_numbers.append(num)
print(list_of_big_numbers)