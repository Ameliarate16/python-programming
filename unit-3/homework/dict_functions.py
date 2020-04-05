def dict_merge(first, second):
    merged = first
    for item in second:
        if item in first:
            #if the item is in both then make a list of the two
            merged[item] = [first[item], second[item]]
        else:
            #otherwise just add the item
            merged[item] = second[item]
    return merged

def list_to_dict(person):
    new_dict = {}
    for item in person:
        #add the first item as key and the second as value 
        new_dict[item[0]] = item[1]
    return new_dict

def reverse_dict(forward):
    reversed = {}
    for item in forward:
        #check for list
        if type(forward[item]) is list:
            #if list, add tuple version
            reversed[tuple(forward[item])] = item
        else:
            #add value as key and key as value
            reversed[forward[item]] = item
    return reversed

def possible_words(words, characters):
    #list of all the discovered words
    found = []
    for word in words:
        valid = True
        for letter in word:
            if letter in characters:
                continue
            else:
                #word cant be made
                valid = False
                break
        if valid:
            found.append(word)
    return found

print(dict_merge({'a': 1, 'b': 2}, {'c': 3, 'd': 4}), dict_merge({'a': 1, 'b': 2}, {'b': 3, 'c': 4}), dict_merge({'x': 'one', 'y': 'two'}, {'x': 1.5, 'y': 3.7}))
print(list_to_dict([['name', 'Alice'], ['job', 'Engineer'], ['city', 'Toronto']]))
print(reverse_dict({'name': 'alicia', 'job':'Engineer', 'city': 'Toronto'}), reverse_dict({'a': [1,2,3], 'b': [4,5,6], 'c':[7,8,9]}))

legal_words = ['go', 'bat', 'me', 'eat', 'goal', 'boy', 'run']
letters = ['e', 'o', 'b', 'a', 'm', 'g', 'l']

print(possible_words(legal_words, letters))