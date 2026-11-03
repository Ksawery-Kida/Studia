equation = input("Tell me the operation you would like to do: ")
number1 = int(input("Tell me the first number: "))
number2 = int(input("Tell me the second number: "))


if equation == "+": 
    print(number1 + number2)

elif equation == "-":
    print(number1 - number2)

elif equation == "*": 
    print(number1 * number2)

elif equation == "/": 
    print(number1 / number2)

else:
    raise ValueError("Invalid number")


