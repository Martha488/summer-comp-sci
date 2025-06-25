
def createAccount(name,balance,accts):
    accts[name] = balance #this is how we add thhings to dictionaries

def closeAccount(name,accts):
    if name in accts.keys():
        accts.pop(name)
    else:
        print("that is not a valid account name")

def withdraw(name,amount,accts):
    if name in accts.keys():
        if amount > accts[name]:
            print("amount exceeds account balance")
            return False
        else:
            accts[name] = accts[name] - amount
            return True
    else:
        print("that is not a valid account name")
        return False

def deposit(name,amount,accts):
    if name in accts.keys():
        accts[name] = accts[name] + amount
    else:
        print("that is not a valid account name")

def transfer(acct1,acct2,amount,accts):
    if acct1 in accts.keys() and acct2 in accts.keys():
        if withdraw(acct1, amount, accts):
            deposit(acct2, amount, accts)


def printAccounts(accts):
    print("-----Accounts-----")
    for name in accts:
        print(f"account name: {name}    Balance: {accts[name]}")
def main():
    accounts = {"John Pork":500}
    check = True
    while check == True:
        print("welcome to the bank!")
        print("1. Create Account")
        print("2. Close Account")
        print("3. Withdraw")
        print("4. Deposit")
        print("5. Transfer")
        print("6. Quit")
        
        option = input("Enter your option from the list above: ")
        if option.isnumeric():
            option = int(option)
            
            if int(option) == 1:
                acctname = input("enter the name of your account: ").strip()
                balance = float(input("enter your balance: "))
                createAccount(acctname,balance,accounts)
                printAccounts(accounts)
            elif int(option) == 2:
                acctname = input("enter the name of the account you wish to close: ").strip()
                closeAccount(acctname,accounts)
                printAccounts(accounts)
            elif int(option) == 3:
                acctname = input("enter the account name you wish to withdraw from: ").strip()
                amt = float(input("enter the amount you wish to withdraw: "))
                withdraw(acctname,amt,accounts)
                printAccounts(accounts)
            elif int(option) == 4:
                acctname = input("enter the account name you wish to deposit to: ").strip()
                amt = float(input("enter the amount you wish to deposit: "))
                deposit(acctname,amt,accounts)
                printAccounts(accounts)
            elif int(option) == 5:
                acct1=input("enter the account name you wish to transfer from: ").strip()
                acct2=input("enter the account name you wish to transfer to: ").strip()
                amt = float(input("enter the amount you wish to transfer: "))
                transfer(acct1,acct2,amt,accounts)
                printAccounts(accounts)
            if int(option) == 6:
                print("thanks for visiting!")
                check = False


if __name__ == "__main__":
    main()