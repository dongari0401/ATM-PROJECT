from ATMLAST import DepositError , WithdrawError , InsufficentError
amt=1000
def deposit_money():
    dep_amt=float(input("Enter The Amount You Want to Deposit:"))
    if dep_amt <= 0:
        raise DepositError
    else:
        global amt
        amt=amt+dep_amt
        print("In Your Account Number:XXX123 was Credited INR:{}".format(dep_amt))
        print("In Your Account Number:XXX123 was Current INR:{}".format(amt))

def withdraw_money():
    global amt
    wtd_amt=float(input("Enter the Amount you want to Withdraw:"))
    if wtd_amt <= 0:
        raise WithdrawError
    elif wtd_amt+1000 > amt:
        raise InsufficentError
    else:

        amt=amt-wtd_amt
        print("Your Account Debited with Withdraw INR:{}".format(wtd_amt))
        print("Your Account Current  INR:{}".format(amt))
def balance_enquiry():
    print("Current Balance in Your Account INR:{}".format(amt))