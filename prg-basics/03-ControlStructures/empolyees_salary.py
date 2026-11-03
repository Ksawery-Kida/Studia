import questionary

basic_salary = 5000
bonus = 0.30
is_bonus = questionary.confirm('Did you receive a bonus?').ask()

if is_bonus:
    total_salary = basic_salary + (basic_salary * bonus)
else:
    total_salary = basic_salary

print(f"Basic salary: {basic_salary}")
print(f"Total salary: {total_salary}")

if is_bonus:
    print(f"The bonus: {bonus}")
else:
    print("Unfortunately, you did not receive a bonus.")
