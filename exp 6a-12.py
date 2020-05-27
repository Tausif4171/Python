
#Name: Tausif Khan
#Rollno: 12
#Branch: SE/COMPS 
#Subject - OSTL 
#Div: B



'''
A Python program to create a Bank class where deposits and withdrawals can be handled by using instance methods

'''

class Bank_Account: 
    def __init__(self): 
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine") 
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdraw:", amount) 
        else: 
            print("\n Insufficient balance  ") 
  
    def display(self): 
        print("\n Net Available Balance=",self.balance)

s = Bank_Account()
s.deposit() 
s.withdraw() 
s.display()

'''

Output:-

Hello!!! Welcome to the Deposit & Withdrawal Machine
Enter amount to be Deposited: 20000

 Amount Deposited: 20000.0
Enter amount to be Withdrawn: 4500

 You Withdraw: 4500.0

 Net Available Balance= 15500.0

'''
