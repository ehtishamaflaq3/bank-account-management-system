# Bank Account Management System
# Features:
# Create account
# Deposit/Withdraw money
# Show balance
# Apply interest (for savings accounts)
#                                   [BANK CLASS]
# Store & handle common features for all accounts.
class BankAccount:
    def __init__(self):
        self.acc_num=" "
        self.acc_holder_name=" "
        self.balance=0.0
    
    def create_acc(self):
        while True:
            print("=======CREATE ACCOUNT=======")
            try:
                self.acc_num = int(input("WRITE ACCOUNT NUMBER: "))
                break
            except ValueError:
                    print("Invalid number. Please enter digits only.")
        self.acc_holder_name=str(input("WRITE ACCOUNT HOLDER NAME:- "))
        while True:
            try:
                starting_balance=float(input("STARTING BALANCE:- "))
                if starting_balance<0:
                    print("BALANCE CANNOT BE LESS THAN ZER0")
                    continue
                self.balance=starting_balance
                break
            except ValueError:
                print("PLEASE ENTER A VALID AMOUNT")
        print(f"Account for {self.acc_holder_name} created successfully with balance {self.balance}.")
    
    def deposit(self):
        try:
            user_deposit_amount=float(input("WRITE THE AMOUNT:- "))
            if user_deposit_amount<=0:
                print("AMOUNT NOT EQUAL OR LESS THAN ZERO")
                return
            print(f"YOUR  PREVIOUS BALANCE IS {self.balance}")
            self.balance=self.balance+user_deposit_amount
            print(f"YOU DEPOSIT {user_deposit_amount}, YOUR TOTAL BALANCE IS {self.balance}")
        except ValueError:
            print("PLEASE ENTER A VALID AMOUNT")    
    def withdraw(self):
        try:
            user_withdraw_amount=float(input("WRITE WITHDRAWL AMOUNT:- "))
            if user_withdraw_amount<=0:
                print("AMOUNT MUST BE GREATER THEN ZERO")
                return
            if user_withdraw_amount>self.balance:
                print("INSUFFICENT BALANCE")
                return
            print(f"YOUR PREVIOUS BALANCE IS {self.balance}.")
            self.balance=self.balance-user_withdraw_amount
            print(f"YOU WITHDRAW {user_withdraw_amount} AMOUNT,NOW YOUR TOTAL BALANCE IS {self.balance}")
        except:
            print("PLEASE ENTER A VALID AMOUNT")
    def show_balance(self):
        print(f"YOUR BALANCE IS:- {self.balance}")

class SavingAccount(BankAccount):
    def __init__(self):
        super().__init__()
    
    def interest_rate(self,rate):
        if rate<0:
            print("INTEREST RATE CANNOT IN NEGATIVE")
            return
        interest=self.balance *(rate/100)
        self.balance+=interest
        print(f"Interest of {interest:.2f} added. New balance: {self.balance:.2f}")

# Assuming accounts list stores BankAccount or SavingAccount objects
def print_all_accounts(accounts):
    if not accounts:
        print("No accounts available.")
        return
    print("\n=== All Accounts ===")
    for i, acc in enumerate(accounts, start=1):
        print(f"{i}. Account Holder: {acc.acc_holder_name} .")
        print(f"   Account Number: {acc.acc_num}")
        # print(f"   Account Type: {acc.acc_type}")
        print(f"   Balance: {acc.balance:.2f}")
        print("-" * 30)
# ----------------------DATA SECTION----------------------------
def save_data(accounts,savingaccounts):
    with open("accounts.txt","w") as file:
        for acc in accounts:
            file.write(f"SIMPLE,{acc.acc_num},{acc.acc_holder_name},{acc.balance}\n")
        for s in savingaccounts:
            file.write(f"SAVING,{s.acc_num},{s.acc_holder_name},{s.balance}\n")
def load_data():
    accounts=[]
    savingaccounts=[]
    try:
        with open("accounts.txt","r") as file:
            for line in file:
                parts=line.strip().split(",")
                if len(parts) != 4:  # skip if not correct
                    continue
                acc_type,acc_num,acc_holder_name,balance=parts
                if acc_type=="SIMPLE":
                    acc=BankAccount()
                    accounts.append(acc)
                elif acc_type=="SAVING":
                    acc=SavingAccount()
                    savingaccounts.append(acc)
                else:
                    continue
                acc.acc_holder_name=acc_holder_name
                acc.acc_num=int(acc_num)
                acc.balance=float(balance)
    except FileNotFoundError:
        pass
    return accounts,savingaccounts                
        
def main():
    accounts,savingaccounts=load_data()
    while True:
        print("1.CREATE ACCOUNT")
        print("2.DEPOSIT MONEY")
        print("3.WITHDRAW MONEY")
        print("4.SHOW BALANCE")
        print("5.APPLY INTEREST")
        print("6.SEE ALL ACCOUNTS")
        print("7.SAVE & EXIT")
        try:
            choice=int(input("WRITE THE SERVICE YOU WANT(1-6):- "))
        except ValueError:
            print("INVALID CHOICE,PLEASE ENTER A NUMBER")
            continue
        match choice:
            case 1:
                print("1.CREATE SIMPLE ACCOUNT")
                print("2.CREATE SAVING ACCOUNT")
                try:
                    choices=int(input("YOUR CHOICE:- "))
                except:
                    print("INVALID CHOICE,PLEASE ENTER A NUMBER")
                    continue
                match choices:
                    case 1:
                        acc=BankAccount()
                        acc.create_acc()
                        accounts.append(acc)
                    case 2:
                        s=SavingAccount()
                        s.create_acc()
                        savingaccounts.append(s)
            case 2:
                try:
                    acc_num=int(input("ENTER ACCOUNT NUMBER:- "))
                except ValueError:
                    print("INVALID INPUT")
                    continue
                for acc in accounts + savingaccounts:
                    if acc.acc_num==acc_num:
                        acc.deposit()
                        break
                else:
                    print("ACCOUNT NOT FOUND")
                
            case 3:
                try:
                    acc_num=int(input("ENTER ACCOUNT NUMBER:- "))
                except ValueError:
                    print("INVALID INPUT")
                    continue
                for acc in accounts + savingaccounts:
                    if acc.acc_num==acc_num:
                        acc.withdraw()
                        break
                else:
                    print("ACCOUNT NOT FOUND")
            case 4:
                try:
                    acc_num = int(input("ENTER ACCOUNT NUMBER:- "))
                except:
                    print("INVALID INPUT")
                    continue
                for acc in accounts + savingaccounts:
                    if acc.acc_num == acc_num:
                        acc.show_balance()
                        break
                else:
                    print("Account not found.")
            case 5:
                try:
                    acc_num = int(input("ENTER SAVING ACCOUNT NUMBER:- "))
                except ValueError:
                    print("INVALID INPUT")
                    continue
                for acc in savingaccounts:
                    if acc.acc_num == acc_num:
                        acc.interest_rate(6)
                        break
                else:
                    print("Saving account not found.")
            case 6:
                print("1.SIMPLE ACCOUNT")
                print("2.SAVING ACCOUNT")
                try:
                    choicessee=int(input("YOUR CHOICE:- "))
                except ValueError:
                    print("INVALID INPUT")
                    continue
                match choicessee:
                    case 1:
                        print_all_accounts(accounts)
                    case 2:
                        print_all_accounts(savingaccounts)
            case 7:
                save_data(accounts,savingaccounts)
                break
            case _:
                print("INVALID CHOICE")

main()