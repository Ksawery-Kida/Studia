class Height:
    def __init__(self, feet, inches, cm): 
        self.feet = feet
        self.inches = inches
        self.cm = cm

    def ask_height(self):
        while True: 
            try: 
                cm= int(input("Enter height in centimeters: "))
                if cm < 0:
                    print("Height cannot be negative. Please try again.")
                else:
                    self.cm = cm
                    break
            except ValueError:
                print("That's not a valid number. Please try again.")

    def cm_to_inches(self):
        return self.cm // 2.54

    
    def cm_to_feet(self):
        return self.cm // 30.48

    def call(self):
        print(
            f"{self.cm} cm is equal to approximately {self.cm_to_inches()} inches and approximately {self.cm_to_feet()} feet.")
            
if __name__ == "__main__":
    h = Height (0,0,0)
    h.ask_height()
    h.call()