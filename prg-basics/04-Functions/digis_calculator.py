class Digits:

    def __init__(self, number, count):
        
        self.number = number
        self.count = count

    
    def ask_input(self):
        self.number = int(input("Tell me the number: "))

    
    
    def sum_digits(self):
        for i in range(len(str(self.number))):
            self.count.append(int(str(self.number)[i]))
        print(f"The sum of the digits is: {sum(self.count)}")


if __name__ == "__main__":
    d = Digits(0, [])
    d.ask_input()
    d.sum_digits()