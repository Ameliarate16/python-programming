'''
def add_two():
    result = 5 + 5
    print(result)

#passing arguments
def add_two(a, b):
    result = a + b
    print(result)

#returning the value
def add_two(a, b):
    result = a + b
    return result

print(add_two(3, 10))
'''

#write a function that returns the sum of the integers in a list
def sum_list(a_list):
    running_sum = 0
    for num in a_list:
        running_sum += num
    return running_sum

#print(sum_list([1,-2,3,4,5]))

# write a function that reverses a string
def rev_string(my_string):
    reverse = ""
    for char in my_string:
        reverse = char + reverse
    return reverse

#write a function that finds the intersection of two lists
def intersect_list(list_1, list_2):
    intersection = []
    for item in list_1:
        if item in list_2:
            intersection.append(item)
    return intersection

print(intersect_list([1,2,3,4,5,"c"],[12,4,1,"c",180,3]))