class FuelConsumptionCalculator:
    
    def __init__(self, distance, fuel_consumption):
        self.distance = distance
        self.fuel_consumption = fuel_consumption    
    
    def _ask_for_inputs(self):
        self.driving_mode = input('Enter driving mode (A/M/E):')
        self.distance = int(input('Enter distance in km: '))

    def calculate_fuel_consumption(self):
        if self.driving_mode == 'A' or self.driving_mode == 'a':
            self.fuel_consumption = 7 # liters per 100km

        elif self.driving_mode == 'M' or self.driving_mode == 'm':
            self.fuel_consumption = 9 # liters per 100km

        elif self.driving_mode == 'E' or self.driving_mode == 'e':
            self.fuel_consumption = 12 # liters per 100km

        else:
            raise ValueError('Invalid driving mode')
    def print_fuel_consumption(self):
        fuel_needed = (self.distance / 100) * self.fuel_consumption
        print(f'Fuel needed for {self.distance} km: {fuel_needed:.2f} liters')


if __name__ == "__main__":
    calculator = FuelConsumptionCalculator(0, 0)
    calculator._ask_for_inputs()
    calculator.calculate_fuel_consumption()
    calculator.print_fuel_consumption()
    