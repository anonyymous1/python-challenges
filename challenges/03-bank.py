print("Welcome to Chase bank.")
print("Have a nice day!")

def banking():
    amount = 4000
    print('Your current balance is ' + str(amount))
    what_to_do = input('What would you like to do? (deposit, withdraw, check_balance) ')
    if what_to_do == "check_balance":
        print(amount)
    elif what_to_do == "deposit":
        amount2 = int(input('How much would you like to ' + what_to_do + "? "))
        print(amount2)
        new_amount = amount + amount2
        print('Your new balance is ' + str(new_amount))
    elif what_to_do == "withdraw":
        amount2 = int(input('How much would you like to ' + what_to_do + "? "))
        new_amount = amount - amount2
        print('Your new balance is ' + str(new_amount))
    else:
        print('Im sorry, i cant ' + what_to_do)
        
banking()