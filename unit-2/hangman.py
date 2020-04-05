import random

list_of_words = ["south", "silo", "heaven", "girl", "phobia", "stellar", "mute"]
max_number_of_guesses = 5

def game():
    current_number_of_guesses = 0
    current_word = random.choice(list_of_words)
    guessed_letters = []
    
    for index in range(len(current_word)):
        guessed_letters.append("_")
    
    while current_number_of_guesses < max_number_of_guesses:
        print (guessed_letters)
        guess = input ("What is your guess?\n")
        
        if guess in current_word:
            for index in range (len(current_word)):
                if current_word[index] == guess:
                    guessed_letters[index] = guess
        else:
            current_number_of_guesses += 1
            print (f"Try again! You have {max_number_of_guesses - current_number_of_guesses} chances left")
        
        if "_" not in guessed_letters:
            break
    
    if current_number_of_guesses == max_number_of_guesses:
        print ("You lose!")
    else:
        print("You win!")

    print(f"The word was: {current_word}")

game()