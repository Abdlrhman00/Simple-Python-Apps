import random

def generate_random():
    return random.choice(range(1,10))

def provide_hint(secret, guess):
    difference = abs(secret - guess)

    if difference > 5:
        print("Not even close.")
    elif difference < 3:
        print("Almost there.")
    else:
        print("Close.")


def play_game():
    secret_number = generate_random()
    guesses = 0

    print("Welcome to the Guessing Game!")
    print("I've picked a number between 1 and 10. Can you guess what it is?")
    
    while guesses < 5:
        guess = int(input('Guess a number between 1 and 10: '))
        guesses += 1
        
        if secret_number == guess:
            print(f"Congratulations! You guessed the correct number ({secret_number}) in {guesses} guesses!")
            return
        
        provide_hint(secret_number , guess)

    print(f"Sorry, you've used all your guesses. The correct number was {secret_number}. Better luck next time!")

play_game()
       
        


