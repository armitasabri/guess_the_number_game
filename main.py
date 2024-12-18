import art
from random import randrange

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

hardiness = input("choose the difficulty. Type 'easy' or 'hard': ")
guessed_right = False
def define_attempts(difficulty):
    if difficulty == 'easy':
        attempts=10
    else:
        attempts=5
    return attempts

def reduce_attempts(remaining_attempts):
    remain = remaining_attempts -1
    return remain

def check_the_guess(real, guessed):
    global guessed_right
    if guessed > real:
        return "Too high"
    elif guessed < real:
        return "Too low"
    else:
        guessed_right = True
        return f"You got it! the answer was {real}"

answer = randrange(1,100)
num_of_attempts = define_attempts(hardiness)

while num_of_attempts >= 1:
    print(f"You have {num_of_attempts} attempts remaining to guess the number")
    guess = int(input("make a guess: "))
    print(check_the_guess(answer,guess))
    if num_of_attempts >=2 and not guessed_right:
        print("guess again")
    if not guessed_right:
        num_of_attempts = reduce_attempts(num_of_attempts)
    else:
        break
else:
    print("you couldn't guessed the right number!")
