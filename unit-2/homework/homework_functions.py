#function to count the number of occurences of a letter in a string
def letter_count(string, letter):
    #count letter in string
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count

#function to count the number of words in a string
def count_words(words):
    #split string into words
    list_words = words.split()
    #return length of list = num of words
    return len(list_words)

#function to reverse a list
def reverse_list(reversable):
    reversed = []
    for item in reversable:
        #put each item at the front of the list
        reversed.insert(0, item)
    return reversed

#function to separate a list into two lists around a pivot
def split_list(splitter, pivot):
    high, low = [], []
    for num in splitter:
        #put numbers greater or equal to the pivot in high, and the rest in low
        if num >= pivot:
            high.append(num)
        else:
            low.append(num)
    #return a list of low and then high
    return [low, high]

#function to check if a string is an isogram
def is_isogram(isogram):
    for char in isogram:
        #if any letter shows up more than once it's not an isogram
        if letter_count(isogram, char) > 1:
            return False
    return True

print(letter_count('abcde', 'a'), letter_count('this is going to be easy', 'i'), letter_count('how about that?', 'z'))
print(count_words('hey there!!'), count_words('I\'m staying home because of the epidemic'), count_words('how-about-a-hypenated-string?'))
print(reverse_list([]), reverse_list([1, 2, 3]), reverse_list(['this', 'is', 'cool!']))
print(split_list([1, 2, 3], 0), split_list([4, 5, 11, 8, 19], 10), split_list([5, 6, 20, -4, -12, 0], -1))
print(is_isogram('abc'), is_isogram('hi there'), is_isogram('Hapy coding!'))