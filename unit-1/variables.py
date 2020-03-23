'''car_total = 13

if car_total % 2 == 1:
    print("I have an odd number of cars.")
else:
    print("I have an even number of cars.")

score = 69

if score >= 80:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 50:
    grade = "C"
else:
    grade = "D"

print(grade)

for num in range(1, 51):
    output = ""
    if num % 3 == 0:
        output += "fizz"
    if num % 5 == 0:
        output += "buzz"
    if output == "":
        output = num
    print(output)

for num in range(1, 51):
    if num % 15 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
'''

#find the sum of even numbers between 1 and 10
total = 0
for num in range(1, 11):
    if num % 2 == 0:
        total += num #calculate running sum

print(total)