import json

cars = [
    {
        'make': 'Toyota',
        'model': 'Camry',
        'year': '2017',
        'color': 'black'
    },
    {
        'make': 'Toyota',
        'model': 'Prius',
        'year': '205',
        'color': 'white'
    },
    {
        'make': 'Mercedes Benz',
        'model': 'A 250',
        'year': '2019',
        'color': 'grey'
    },
    {
        'make': 'Hyundai',
        'model': 'Elantra',
        'year': '2007',
        'color': 'grey'
    },
    {
        'make': 'Lexus',
        'model': 'IS 300',
        'year': '2020',
        'color': 'blue'
    }
]

prices = [1000, 2000, 3000, 4000, 5000]

#for index in range(len(cars)):
#    cars[index]['price'] = prices[index]

for index, car in enumerate(cars):
    car['price'] = prices[index]

#print(json.dumps(cars, indent=2))

state_capitals = {
    "Alaska" : "Juneau",
    "Colorado" : "Denver",
    "Oregon" : "Salem",
    "Texas" : "Austin"
}


def reverse_lookup(dictionary, value):
    for key in dictionary:
        if dictionary[key] == value:
            return key

    return "Value not found"

#print(reverse_lookup(state_capitals, "Salem"))

def frequency_counter(string):
    words = string.split()
    occurrences = {}
    for word in words:
        if word in occurrences:
            occurrences[word] += 1
        
        else:
            occurrences[word] = 1
    
    return occurrences

print(json.dumps(frequency_counter("this is a string that you need to find the the occurences of each word in the string"), indent=1))
