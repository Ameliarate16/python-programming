#Given a string, replace every letter with its position in the alphabet
string = "guess who just got back today? them wild-eyed boys that've been away"

positions = []

for character in string:
    position = ord(character.lower()) - 96
    if position > 0 and position < 27:
        positions.append(position)

print(*positions)