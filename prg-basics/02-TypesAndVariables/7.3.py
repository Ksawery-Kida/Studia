car_number = input("Enter car Number: ")


def registration_numbers(registration):
    if registration[0:2].upper() in ("KR", "KK"):
        print("car is from krakow")
    else: 
        print("car is not from krakow")
registration_numbers(car_number)