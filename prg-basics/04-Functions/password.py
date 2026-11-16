class Password:

    def __init__(self, password):
        self.password = password

    def get_password(self):
        self.password = input("Type down your password: ")

    def validation_1(self):
        # count how many times each character appears
        seen = {}
        for x in self.password:
            if x in seen:
                seen[x] += 1
            else:
                seen[x] = 1
        # any character appearing more than once -> not unique
        for count in seen.values():
            if count != 1:
                return False
        return True

    def validate_password(self):
        if 6 <= len(self.password) and self.validation_1():
            print(f"Password {self.password} is valid")
            return True
        else:
            print(f"Password {self.password} is not valid")
            return False


if __name__ == "__main__":
    c = Password("")
    c.get_password()
    c.validate_password()
