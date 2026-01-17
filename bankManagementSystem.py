import random
import os
import json



class BankAccount:
    
    def __init__(self,id:int,Name:str,Balance:int,Phone_no:int,Address:str,Email:str):
        self.Customerid=id
        self.Name=Name
        self.Balance=Balance
        self.Phone_Number=Phone_no
        self.Address=Address
        self.Email=Email
    
    def CheckBalance(self):
        print(f"Your Balance is {self.Balance}")
        
    def Deposit(self,Amount:int):
        if(Amount<0):
            print("The Amount cannot be Negative.")
        else:
            self.Balance+=Amount
        
        
    def Withdraw(self,Amount:int):
        if(Amount<0):
            print("The Amount cannot be Negative.")
        if(Amount>self.Balance):
            print(f"The Withdrawed Amount entered is More Than the Current Balance(Current Balance:{self.Balance})")
        if(Amount<=self.Balance):
            self.Balance-=Amount
            
    def DisplayUserInformation(self):
        print("Customer ID:",self.Customerid)
        print("Name:",self.Name)
        print("Phone Number:",self.Phone_Number)
        print("Address",self.Address)
        print("Email:",self.Email)
    
    def Save_Accounts(self):
        new_account={'Customer ID':self.Customerid ,'Name':self.Name,'Balance':self.Balance,'Phone Number':self.Phone_Number,'Address':self.Address,'Email':self.Email}
        accounts=BankAccount.load_json()
        new_list=[]
        if not accounts:
            new_list.append(new_account)
        else:
            for account in accounts:
                    if new_account['Customer ID'] == account['Customer ID']:
                        new_list.append(new_account)
                    else:
                        new_list.append(account)
        if new_account not in new_list:
            new_list.append(new_account)
        

                        
                    
        with open("BankAccounts.json",'w') as f:
            json.dump(new_list,f,indent=4)
    
            

    
    @staticmethod
    def load_json():
        if not os.path.exists("BankAccounts.json"):
            return []
        with open("BankAccounts.json","r") as f:
            try:
                return json.load(f) 
            except json.JSONDecodeError:
                return[]
        
    
  
        

class BankServices():
    
    def CreateAccount(self):
        Name= input("Name:")
        Phone_Number=int(input("Phone Number:"))
        Address=input("Address:")
        Email=input("Email:")
        Balance=int(input("Deposit Balance for your Bank account:"))
        if(Balance>0):
            idcount=random.randint(1,1000)
            i=BankAccount(idcount,Name,Balance,Phone_Number,Address,Email)
            i.Save_Accounts()
            print(f"Your Id no For the Bank Account is {idcount}")
        else:
            print("Insufficient Deposit for Opening the Account")
        
    def SearchAccount(self,Phone:int):
        obj=BankAccount.load_json()
        for i in obj:
            if Phone == i['Phone Number']:
                return i    
        print("The Number doesn't exist.") 
        
                
                

        
def main():    
    os.system('cls' if os.name == 'nt' else "clear")
    while True:
        print("\n---Welcome to Banking system---")
        print("1.Bank Services")
        print("2.Exit")
        option=int(input("Choose An Option: "))
        if (option==1) :
            os.system('cls' if os.name == 'nt' else "clear") 
            bankServ()
        elif (option==2):
            os.system('cls' if os.name == 'nt' else "clear") 
            print("Exitted this program sucessfully")
            return False
        else:
            os.system('cls' if os.name == 'nt' else "clear") 
            print("Enter the input Correctly")
            
        
        
        
    

    
def bankServ():
    a=BankServices()
    while True:
        print("\n---Welcome to bank services---")
        print("1.Create Account")
        print("2.Search Account")
        print("3.Exit")
        option=int(input("Choose An Option: "))
        if (option==1):
            a.CreateAccount()
        elif (option == 2):
            Phone=int(input("Enter the phone Number:"))
            i=a.SearchAccount(Phone) 
            if i is None:
                print("Account not found.Returning to Menu")
                continue
            Account(i)   
        elif (option ==3):
            print("Exitted this program sucessfully")
            break
        else:
            print("Enter the input Correctly")
        
        
    
def Account(i:dict):
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
            b.Save_Accounts()
        elif (option == 2):
            os.system('cls' if os.name == 'nt' else "clear")  
            b.Withdraw(int(input("Enter The Withdrawal Amount:")))
            b.Save_Accounts()
        elif (option == 3):
            os.system('cls' if os.name == 'nt' else "clear") 
            b.CheckBalance()
        elif (option == 4):
            os.system('cls' if os.name == 'nt' else "clear") 
            b.DisplayUserInformation()    
        elif (option ==5):
            print("Exitted this program sucessfully")
            return False
        else:
            print("Enter the input Correctly")
            
            
if __name__ =="__main__":
    main()
    
            