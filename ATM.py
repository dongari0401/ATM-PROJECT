import sys
from ATMOP import deposit_money , withdraw_money , balance_enquiry
from ATMLAST import DepositError , WithdrawError ,InsufficentError
from ATMDEMO import menu

while True:
    menu()
    try:
        mb=int(input("Enter Your Choice:"))
        match(mb):
            case 1:
                try:
                   deposit_money()
                except ValueError:
                    print("Don't Enter Str , Complex , etc..")
                except DepositError:
                    print("Don't Deposit Zero's and Negative Numbers")
            case 2:
                  try:
                     withdraw_money()
                  except WithdrawError:
                      print("Check Your Balance Enter Minimum Amount, Withdraw ERRor")
                  except InsufficentError:
                      print("Check Your  Balance Once ! , Insufficent Money in Account ")

            case 3:balance_enquiry()
            case 4:
                   print("Program successfully running")
                   sys.exit()
            case _:
                print("Invalid Choice Make Choose Again:")
    except ValueError:
        print("Don't Enter Str , Complex , Etc...")