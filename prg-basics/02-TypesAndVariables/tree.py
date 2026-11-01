print("welcome to the program that'll tell you if the tree is eligible to be cut")
height = int(input("enter the height: "))

def tree_height(height):
    if height <= 50: 
        print("The tree is not eligible")
    else: 
        print("The tree is eligible")


tree_height(height)

    