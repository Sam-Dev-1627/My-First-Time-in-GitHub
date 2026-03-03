import random   
secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("Can you guess it?")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too Low! Try again.")
    elif guess > secret_number:
        print("Too High! Try again.")
    else:
        print("Congratulations! You guessed it correctly.")
        print("Number of attempts:", attempts)
        break