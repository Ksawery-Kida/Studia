class BinaryCalculator:
    
    def __init__(self, number): 
        self.number = number

    
    def ask_number(self):
        while True:
            try:
                number = input("Enter yournumber: ")
                if not number.isdigit():
                    print("That's not a valid number. Please try again.")
                else:
                    self.number = int(number)
                    break
            except ValueError:
                print("That's not a valid number. Please try again.")
    
    
    def decimal_to_binary(self):
        return bin(self.number)[2:]


    def decimal_to_hexadecimal(self):
        return hex(self.number)[2:].upper()

    def print_results(self):
        print(f"Decimal: {self.number}")
        print(f"Binary: {self.decimal_to_binary()}")
        print(f"Hexadecimal: {self.decimal_to_hexadecimal()}")

if __name__ == "__main__":
    calculator = BinaryCalculator(0)
    calculator.ask_number()
    calculator.print_results()