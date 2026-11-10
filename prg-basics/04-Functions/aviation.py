''' 
1. The ICAO (International Civil Aviation Organization) phonetic alphabet is used internationally for spelling out letters in radio communication. The icao.py program contains a function that returns the corresponding word for a given letter. Complete the program to spell out a name entered from the keyboard.

1. Define a function `time_string(hours, minutes, time_format)` that, given the number of hours (0..23) and the number of minutes (0..59), returns a string specifying the time in the given format ('24' for 24-hour time and '12' for 12-hour time). 
'''


def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f"{hours:02}:{minutes:02}"
    elif time_format == '12':
        period = 'AM' if hours < 12 else 'PM'
        hours_12 = hours % 12
        hours_12 = 12 if hours_12 == 0 else hours_12
        return f"{hours_12:02}:{minutes:02} {period}"
    else:
        raise ValueError("Invalid time format. Use '24' or '12'.")


def ask_time(time_format):
    while True:
        try:
            hours = int(input("Enter hours (0-23): "))
            minutes = int(input("Enter minutes (0-59): "))
            if 0 <= hours <= 23 and 0 <= minutes <= 59:
                return time_string(hours, minutes, time_format)
            else:
                print("Invalid input. Please enter valid hours and minutes.")
        except ValueError:
            print("Invalid input. Please enter numeric values for hours and minutes.")


if __name__ == "__main__":
    time_format = input(
        "Enter time format ('24' for 24-hour, '12' for 12-hour): ")
    if time_format not in ['24', '12']:
        print("Invalid time format. Please enter '24' or '12'.")
    else:
        time_output = ask_time(time_format)
        print(f"The time is: {time_output}")
