print("welcome to the program that checks wheter the number you enter is even or not")

number = int(input('Enter number: '))

def number_check(number): 
    if number % 2 == 0:
        print("the number you entered is even.")
    else: 
        print("the number you entered is not even.")
number_check(number)
    