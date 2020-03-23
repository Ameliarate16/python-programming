'''
readings = [25, 18, -5, 11, -3, -15, 8, -18, 6, 13]

#count the number of negative readings
count = 0
for temp in readings:
    if temp < 0:
        count += 1
print(count)


#find the average of the positive readings
total = 0
count = 0
for temp in readings:
    if temp > 0:
        count += 1
        total += temp
print(total / count)


titles = ["The Avengers", "Avengers Age of Ultron", "Captain America, The First Avenger"]

#count how many titles have "the" in them
count = 0
for title in titles:
    if "The" in title:
        count += 1
print(f'list has {count} titles with "The"')
'''

#how many vowels are in a string?
string = "There is a long string that has only a few vowels"
count = 0
for char in string:
#    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
#        count += 1
    if char in "aeiou":
        count += 1
print(count)