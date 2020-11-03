import sys
from user.authentication import authenticate_user
import transactions.journal
from transactions.journal import receive_income
from transactions.journal import pay_expense
import banking

if __name__ == "__main__":

    if len(sys.argv) >= 2: # If two or more arguments are entered into commandline,
        print("\n".join(str(i) for i in sys.argv[1:])) # Prints out commandline args, one below the other

    authenticate_user()
    receive_income('100')
    pay_expense('100')
    banking.fvb_recon()