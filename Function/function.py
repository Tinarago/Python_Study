def open_account():
    print("new account created!")

def deposit(balance, money):
    print("deposited. new balance: {}.".format(balance+money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("Withdraw completed. new balance: {}.".format(balance-money))
        return balance - money
    else:
        print("withdraw not completed. balance: {}.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

open_account()
balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
# balnace = withdraw(balance, 500)

commission, balance = withdraw_night(balance, 500)
print("commission is {}, new balance is {}.".format(commission, balance))