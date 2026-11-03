

account_balance = 500
total_payment = int(input("Tell me the total amount of your purchases: "))

if total_payment < account_balance:
    print('Payment completed')

else:
    print('No funds')
