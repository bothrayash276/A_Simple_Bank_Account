# ------------------------------
# Simple Bank Account Program 
# Submittion by Yash Bothra (Associate)
# ------------------------------

import pandas as pd
import random


# Adding a New User
def new_user(name, age, balance):
  
  # Generating Bank Account Number
  bank_number="25"
  num = random.randint(0,10)
  bank_number= bank_number + str(num)
  
  '''
  0 --> Name
  1 --> Age
  2 --> Bank Balance
  '''
  
  new_user_data = {
    f"{bank_number}" : [name,age,balance]  
  }

  print(f"Your Banking Account Number is {bank_number}")

  userExport = pd.DataFrame(new_user_data)
  userExport.to_csv("BankDetails.csv")


# Updating User Data Base
def update_user_details(bank_number,new_balance):
  user_csv = pd.read_csv(f"BankDetails.csv")
  user_csv.loc[bank_number, "Balance"] = new_balance
  user_csv.to_csv("BankDetails.csv")





# Function to display balance
def get_balance(bank_number):
    # TODO: Print the current balance
    userD = pd.read_csv("BankDetails.csv")
    current_balance = userD.loc[2,bank_number]
    print(f"Your Current Balance is {current_balance}")



# Function to deposit money
def deposit(bank_number, amount):
    # TODO: Check if amount is valid
    userD = pd.read_csv("BankDetails.csv")
    current_balance = userD.loc[bank_number,"Balance"]
    if(amount>0):
    # If valid, add to balance
      current_balance += amount
      userD.loc[bank_number,"Balance"] = current_balance
      userD.to_csv("BankDetails.csv")
    else:
    # Otherwise, show error
      print("Invalid Amount Entered!")



# Function to withdraw money
def withdraw(bank_number, amount):
    # TODO: Check if amount is valid and not more than balance
    userD = pd.read_csv("BankDetails.csv")
    current_balance = userD.loc[bank_number, "Balance"]
    if(amount<=current_balance and amount>0):
    # If valid, subtract from balance
      current_balance -= amount
      userD.loc[bank_number,"Balance"] = current_balance
      userD.to_csv("BankDetails")
    # Return updated balance

    else:
    # Otherwise, show error
      print("Invalid Amount Entered")
 







initial_balance = 100

# Create the main program loop with the use of conditionals and loop statements
# D --> Deposit
# W --> Withdraw
# C --> Check balance
# Q --> Quit

# The loop should stop only if user enters Q

print("N --> New User \nD --> Deposit \nW --> Withdraw \nC --> Check balance \nQ --> Quit")

accNum = str(input("Enter your Bank Account Number: "))

while True:
  
  user_choice = str(input("How do you wanna proceed: "))

  # Deposit System
  if(user_choice=='N'):
    user_name = str(input("Enter your Name: "))
    user_age = int(input("Enter your Age: "))
    user_balance = int(input("Enter your initial balance: "))
    new_user(user_name,user_age,user_balance)
    break
  elif(user_choice=='D'):
    user_deposit = int(input("Enter the amount to be deposited: "))
    initial_balance = deposit(accNum,user_deposit)
    get_balance(accNum)

  # Withdrawing System 
  elif(user_choice=='W'):
    user_withdraw = int(input("Enter the amount to be withdrawn: "))
    initial_balance = withdraw(accNum,user_withdraw)
    get_balance(accNum)

  # Checking the Balance System
  elif(user_choice=='C'):
    get_balance(accNum)

  # Exiting the System
  elif(user_choice=='Q'):
    break

  # If input entered other than W,D,C,Q
  else:
    print("Invalid Input!")
    continue
  
  # Keeping the code clear
  print("\n")


