'''
numbers = [8, 5, 17]

#insert the number -5 at the front of the list
numbers.insert(0, -5)

#find the number of elements in the list
print(len(numbers))

#remove the last element in the list
last_el = numbers.pop()
print(last_el)

#print the second element in the list
print(numbers[1])

grades = [70, 85, 91, 23, 60, 45, 90, 56, 77, 88]

#add 5 to each grade in the list
for index in range(len(grades)):
    grades[index] += 5
print(grades)
'''
#make each word in this list past tense
verbs = ["like", "hate", "fake", "rake"]
for index in range(len(verbs)):
    verbs[index] += 'd'
print(verbs)

classmates = ["amelia", "abdul", "harrison", "long", "donyell", "kate"]