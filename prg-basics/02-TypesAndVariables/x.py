import random


class DiceGame():
    def __init__(self, sides=6):
        self.sides = sides
        self.computer_roll = None
        self.guess = None
    

    def roll(self):
        self.computer_roll = random.randint(1, self.sides)

    def ask_guess(self):
        while True:
            try:
                guess = int(input(f"Enter your guess (1-{self.sides}): "))
            except ValueError:
                print("That's not a number. Try again.")
                continue

            if 1 <= guess <= self.sides:
                self.guess = guess
                return
            print(f"Your guess must be between 1 and {self.sides}.")

    def is_correct(self):
        return self.guess == self.computer_roll

    def play(self):
        print("Welcome to the program where you can try to guess the number that got rolled by the computer!")
        self.ask_guess()
        self.roll()
        print(f"The computer rolled: {self.computer_roll}")
        if self.is_correct():
            print("Congratulations! You guessed correctly.")
        else:
            print("Sorry, you didn't guess correctly.")


def main():
    game = DiceGame()
    game.play()


if __name__ == "__main__":
    main()


'''
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
'''
