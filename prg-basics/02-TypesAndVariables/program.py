from random import randint

print("Welcome to the program that'll print the results of the amount of dice rolls you choose!")
amount = int(input("Enter the amount of dice rolls: "))


def roll_the_dice_calculator(result,):
    for i in range(result):
        print(randint(1, 6))
    
roll_the_dice_calculator(amount)