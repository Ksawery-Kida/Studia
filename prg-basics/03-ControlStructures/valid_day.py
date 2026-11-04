class ValidDay:
    def __init__(self, day):
        self.day = day

    def get_day(self):
        self.day = int(input("Enter a day number (1-31): "))
    
    def is_valid(self):
        if 1 <= self.day <= 31:
            print(f"Day {self.day} is valid.")
        else:
            print("Invalid day number")

    def print_day(self):
        print(f"The day you entered is: {self.day}")

if __name__ == "__main__":
    day_instance = ValidDay(0)
    day_instance.get_day()
    day_instance.is_valid()
    day_instance.print_day()