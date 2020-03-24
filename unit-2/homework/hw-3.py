odd_strings = ['abba', '111', 'canal', 'level', 'abc', 'racecar', '123451' , '0.0', 'papa', '-pq-']
count = 0

for odd_string in odd_strings:
    #check if length > 3 and first and last characters are the same
    if len(odd_string) > 3 and odd_string[0] == odd_string[-1]:
        count += 1

print(count)