class BankCode: 
    
    
    def __init__(self, bank_code, country_code, location_code, branch_code):
        self.bank_code = bank_code
        self.country_code = country_code
        self.location_code = location_code
        self.branch_code = branch_code

    
    def ask_bank_code(self): 
        while True:
            try:
                bank_code = input("Enter a bank code (4 letters): ")
                if len(bank_code) != 4 or not bank_code.isalpha():
                    print("Bank code must be 4 letters. Please try again.")
                else:
                    self.bank_code = bank_code.upper()
                    break
            except ValueError:
                print("That's not a valid bank code. Please try again.")
    
    
    def ask_country_code(self):
        while True:
            try:
                country_code = input("Enter a country code (2 letters): ")
                if len(country_code) != 2 or not country_code.isalpha():
                    print("Country code must be 2 letters. Please try again.")
                else:
                    self.country_code = country_code.upper()
                    break
            except ValueError:
                print("That's not a valid country code. Please try again.")
    
    
    def ask_location_code(self):
        while True:
            try:
                location_code = input("Enter a location code (2 letters): ")
                if len(location_code) != 2 or not location_code.isalpha():
                    print("Location code must be 2 letters. Please try again.")
                else:
                    self.location_code = location_code.upper()
                    break
            except ValueError:
                print("That's not a valid location code. Please try again.")
    
    
    def ask_branch_code(self):
        while True:
            try:
                branch_code = input("Enter a branch code (3 letters): ")
                if len(branch_code) != 3 or not branch_code.isalpha():
                    print("Branch code must be 3 letters. Please try again.")
                else:
                    self.branch_code = branch_code.upper()
                    break
            except ValueError:
                print("That's not a valid branch code. Please try again.")
    
    
    def call(self):
        print(
            f"Bank code: {self.bank_code}, Country code: {self.country_code}, Location code: {self.location_code}, Branch code: {self.branch_code}.")

if __name__ == "__main__":
    bc = BankCode("", "", "", "")
    bc.ask_bank_code()
    bc.ask_country_code()
    bc.ask_location_code()
    bc.ask_branch_code()
    bc.call()