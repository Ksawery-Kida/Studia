def day_name(day_number):
    if day_number == 1:
        result = 'Monday'
    elif day_number == 2:
        result = "Tuesday"
    elif day_number == 3:
        result = "Wednesday"
    elif day_number == 4:
        result = "Thursday"
    elif day_number == 5:
        result = "Friday"
    elif day_number == 6:
        result = "Saturday"
    elif day_number == 7:
        result = "Sunday"
    else:
        result = None

    return result


def ask_for_day_number(day_number=None):
    if day_number is None:
        day_number = int(input("Enter a number between 1 and 7: "))
    if day_number < 1 or day_number > 7:
        print("Invalid input. Please enter a number between 1 and 7.")
        return ask_for_day_number()
    return day_number

if __name__ == "__main__":
    day_number = ask_for_day_number()
    day = day_name(day_number)
    print(f"The day corresponding to {day_number} is {day}.")
