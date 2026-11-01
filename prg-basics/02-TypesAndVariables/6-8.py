import string

print("this is a program to count the distance between two letters in the alphabet")
input1 = input("Enter the first letter: ").lower()
input2 = input("Enter the second letter: ").lower()


def distance_letters(input1, input2):
    if (len(input1) != 1 or len(input2) != 1
            or input1 not in string.ascii_lowercase
            or input2 not in string.ascii_lowercase):
        raise ValueError("Both inputs must be single letters from a to z.")
    between = max(abs(ord(input1) - ord(input2)) - 1, 0)
    print(f"Between {input1} and {input2} there are {between} letters")


distance_letters(input1, input2)
