#Given a string of words, determine the length of the shortest word
string = "three five sixteen twelve aaaaaaaaa"

split = string.split()
shortest = len(split[0])

for word in split:
    if len(word) < shortest:
        shortest = len(word)

print(shortest)