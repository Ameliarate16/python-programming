odd_strings = ['abba', '111', 'canal', 'level', 'abc', 'racecar', '123451' , '0.0', 'papa', '-pq-']
count = 0

for odd_string in odd_strings:
    #record length for ease of use
    length = len(odd_string)
    #check if length > 3 and first and last characters are the same
    if length > 3 and odd_string[0] == odd_string[length - 1]:
        count += 1

print(count)