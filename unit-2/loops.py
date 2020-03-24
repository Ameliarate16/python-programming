'''
secret = 5
input_value = int(input("Guess the number: "))

while input_value != secret:
    input_value = int(input("Wrong! Guess again. "))


#check if string is palindrome
string = "abcba"
parseable_string = list(string)
palindrome = True

while len(parseable_string) > 1:
    if parseable_string.pop(0) != parseable_string.pop():
        palindrome = False
        break

if palindrome == True:
    print("Palindrome")
else:
    print("Not palindrome")

'''

#check if string is palindrome
string = "abba"
reverse = ""
index = len(string) - 1

while index >= 0:
    reverse += string[index]
    index -= 1

if string == reverse:
    print("Palindrome")
else:
    print("Not palindrome")