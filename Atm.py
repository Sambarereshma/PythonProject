print("Insert Your ATM")
a="yes"
b="no"
balance = 50000
c=input("select any option:-")
pin = 5678

if c == a:
    print("1:cash Withdraw\n2:Balance enquery\n3:Pin change")
    e=int(input("please select input"))

    if e == 1:
        amount = int(input("enter amount"))
        print(amount)
        if amount <= balance:
            if amount == 100:
                balance = balance - 100
                print("your current balance is",balance)
            elif amount == 200:
                balance = balance - 200
                print("your current balance is",balance)
            elif amount == 500:
                balance = balance - 500
                print("your current balance is",balance)
            elif amount == 1000:
                balance = balance - 1000
            print("your current balance is",balance)
        elif amount > balance:
            print("your entering balance is invalid")
            print("please try again")
    elif e == 2:
        print("your current balance is", balance)
    elif e == 3:
        tpin = int(input("enter your pin"))
        if tpin == pin:
            cpin = int(input("enter your new pin"))
            print("your pin is suceesfully update")
        elif tpin != pin:
            print("pin is incorrect\nplease try again")
else:
    print("Thank you for visiting")




