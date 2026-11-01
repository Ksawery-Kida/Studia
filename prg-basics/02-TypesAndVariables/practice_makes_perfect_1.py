class Temperature:
    
    def __init__(self, celsius):
        self.celsius = celsius
        self.temperature = celsius

    def ask_temperature(self):
        while True:
            try:
                celsius = float(input("Enter a temperature in Celsius: "))
                self.celsius = celsius
                self.temperature = celsius
                return
            except ValueError:
                print("That's not a valid number. Please try again.")

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    
    def to_kelvin(self):
        return self.celsius + 273.15

    
    def call(self):
        print(
            f"{self.celsius}°C is equal to {self.to_fahrenheit()}°F and {self.to_kelvin()}K.")


if __name__ == "__main__":
    t = Temperature(0)      
    t.ask_temperature()     
    t.call()                
