import random  # For generating random customer IDs
import os      # For clearing the console
import json    # For saving/loading accounts in JSON


# ---------------------- Bank Account Class ----------------------
class BankAccount:
    
    # Initialize the bank account with details
    def __init__(self,id:int,Name:str,Balance:int,Phone_no:int,Address:str,Email:str):
        self.Customerid=id
        self.Name=Name
        self.Balance=Balance
        self.Phone_Number=Phone_no
        self.Address=Address
        self.Email=Email
    
    # Display the current balance
    def CheckBalance(self):
        print(f"Your Balance is {self.Balance}")
        
    # Deposit money into account
    def Deposit(self,Amount:int):
        if(Amount<0):
            print("The Amount cannot be Negative.")
        else:
            self.Balance+=Amount  # Add amount to balance
        
    # Withdraw money from account
    def Withdraw(self,Amount:int):
        if(Amount<0):
            print("The Amount cannot be Negative.")
        if(Amount>self.Balance):
            print(f"The Withdrawed Amount entered is More Than the Current Balance(Current Balance:{self.Balance})")
        if(Amount<=self.Balance):
            self.Balance-=Amount  # Subtract amount from balance
            
    # Display all account details
    def DisplayUserInformation(self):
        print("Customer ID:",self.Customerid)
        print("Name:",self.Name)
        print("Phone Number:",self.Phone_Number)
        print("Address",self.Address)
        print("Email:",self.Email)
    
    # Save or update accounts in the JSON file
    def Save_Accounts(self):
        new_account={'Customer ID':self.Customerid ,'Name':self.Name,'Balance':self.Balance,'Phone Number':self.Phone_Number,'Address':self.Address,'Email':self.Email}
        accounts=BankAccount.load_json()  # Load existing accounts
        new_list=[]
        if not accounts:  # If no accounts exist, add new account
            new_list.append(new_account)
        else:
            for account in accounts:
                    if new_account['Customer ID'] == account['Customer ID']:
                        new_list.append(new_account)  # Update existing account
                    else:
                        new_list.append(account)  # Keep other accounts
        if new_account not in new_list:
            new_list.append(new_account)  # Append if not already in list
        # Write updated accounts to file
        with open("BankAccounts.json",'w') as f:
            json.dump(new_list,f,indent=4)
    
    # Load accounts from JSON file
    @staticmethod
    def load_json():
        if not os.path.exists("BankAccounts.json"):
            return []  # Return empty list if file doesn't exist
        with open("BankAccounts.json","r") as f:
            try:
                return json.load(f)  # Return loaded JSON data
            except json.JSONDecodeError:
                return[]  # Return empty list if file is empty or invalid
        

# ---------------------- Bank Services Class ----------------------
class BankServices():
    
    # Create a new bank account
    def CreateAccount(self):
        Name= input("Name:")
        Phone_Number=int(input("Phone Number:"))
        Address=input("Address:")
        Email=input("Email:")
        Balance=int(input("Deposit Balance for your Bank account:"))
        if(Balance>0):  # Check for valid initial deposit
            idcount=random.randint(1,1000)  # Generate random ID
            i=BankAccount(idcount,Name,Balance,Phone_Number,Address,Email)  # Create account object
            i.Save_Accounts()  # Save account to JSON
            print(f"Your Id no For the Bank Account is {idcount}")
        else:
            print("Insufficient Deposit for Opening the Account")
        
    # Search for an account by phone number
    def SearchAccount(self,Phone:int):
        obj=BankAccount.load_json()  # Load all accounts
        for i in obj:
            if Phone == i['Phone Number']:
                return i  # Return account dictionary if found
        print("The Number doesn't exist.")  # If not found
        

# ---------------------- Main Program ----------------------
def main():    
    os.system('cls' if os.name == 'nt' else "clear")  # Clear console
    while True:
        print("\n---Welcome to Banking system---")
        print("1.Bank Services")
        print("2.Exit")
        option=int(input("Choose An Option: "))
        if (option==1) :
            os.system('cls' if os.name == 'nt' else "clear") 
            bankServ()  # Go to bank services menu
        elif (option==2):
            os.system('cls' if os.name == 'nt' else "clear") 
            print("Exitted this program sucessfully")
            return False
        else:
            os.system('cls' if os.name == 'nt' else "clear") 
            print("Enter the input Correctly")
            

# ---------------------- Bank Services Menu ----------------------
def bankServ():
    a=BankServices()
    while True:
        print("\n---Welcome to bank services---")
        print("1.Create Account")
        print("2.Search Account")
        print("3.Exit")
        option=int(input("Choose An Option: "))
        if (option==1):
            a.CreateAccount()  # Call create account method
        elif (option == 2):
            Phone=int(input("Enter the phone Number:"))
            i=a.SearchAccount(Phone)  # Search account by phone
            if i is None:
                print("Account not found.Returning to Menu")
                continue
            Account(i)  # Go to account menu for found account
        elif (option ==3):
            print("Exitted this program sucessfully")
            break
        else:
            print("Enter the input Correctly")
        

# ---------------------- Individual Account Menu ----------------------
def Account(i:dict):
    # Create BankAccount object from dictionary
    b=BankAccount(i['Customer ID'],i['Name'],i['Balance'],i['Phone Number'],i['Address'],i['Email'])
    while True:
        print("\n---Choose An Option---")
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Check Balance")
        print("4.User Information")  
        print("5.Exit")
        option=int(input("Choose An Option:"))   
        if (option==1):
            os.system('cls' if os.name == 'nt' else "clear") 
            b.Deposit(int(input("Enter The deposit Amount:")))
            b.Save_Accounts()  # Save updated account after deposit
        elif (option == 2):
            os.system('cls' if os.name == 'nt' else "clear")  
            b.Withdraw(int(input("Enter The Withdrawal Amount:")))
            b.Save_Accounts()  # Save updated account after withdrawal
        elif (option == 3):
            os.system('cls' if os.name == 'nt' else "clear") 
            b.CheckBalance()  # Show current balance
        elif (option == 4):
            os.system('cls' if os.name == 'nt' else "clear") 
            b.DisplayUserInformation()  # Show account info   
        elif (option ==5):
            print("Exitted this program sucessfully")
            return False
        else:
            print("Enter the input Correctly")
            

# ---------------------- Program Entry ----------------------
if __name__ =="__main__":
    main()  # Start the banking program
