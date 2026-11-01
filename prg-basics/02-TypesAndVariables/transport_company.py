'''
A transport company needs a program to calculate the cost of transporting goods.
The program calculates the cost of transporting goods based on the given distance in km,
fuel price per 1 liter, and fuel consumption in liters per 100 km. Write such program.
'''


class Transport:

    def __init__(self, distance, fuel_price, fuel_consumption):
        self.distance = distance
        self.fuel_price = fuel_price
        self.fuel_consumption = fuel_consumption

    def ask_distance(self):
        while True:
            try:
                distance = int(input("Please tell me the distance that you'd like to go: "))
            except ValueError:
                print("That's not a number. Please try again.")
                continue
            if distance < 0:
                print("Please give me the correct distance (it can't be negative).")
                continue
            self.distance = distance
            break

    def ask_fuel_price(self):
        while True:
            try:
                fuel_price = float(input("please tell me what the current price of the fuel is /liter: "))
            except ValueError:
                print("That's not a number. Please try again.")
                continue
            if fuel_price < 0 or fuel_price > 10:
                print("Please give me the correct price (between 0 and 10).")
                continue
            self.fuel_price = fuel_price
            break

    def ask_fuel_consumption(self):
        while True:
            try:
                fuel_consumption = float(input("Please tell me the amount of fuel consumtpion in the vehicle ur willing to go on a trip with: "))
            except ValueError:
                print("That's not a number. Please try again.")
                continue
            if fuel_consumption <= 0 or fuel_consumption >= 75:
                print("Please give me the correct consumption (more than 0 and less than 75).")
                continue
            self.fuel_consumption = fuel_consumption
            break

    def print_results(self):
        print(f" The total cost of the trip is: {self.distance * self.fuel_price * self.fuel_consumption / 100} ")


if __name__ == "__main__":
    tc = Transport(0, 0, 0)
    tc.ask_distance()
    tc.ask_fuel_price()
    tc.ask_fuel_consumption()
    tc.print_results()
