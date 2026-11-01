import random

print("Welcome to the program where you can try to guess the number that got rolled by the computer!")
you = input("Enter your guess (1-6): ")
you = int(you)

def main(you):
    computer = random.randint(1, 6)
    print(f"The computer rolled: {computer}")
    if you == computer:
        print("Congratulations! You guessed correctly.")
    else:
        try:
            if you < 1 or you > 6:
                raise ValueError("Your guess must be between 1 and 6.")
        except ValueError as e:
            print(e)
        print("Sorry, you didn't guess correctly.")
    

main(you) 