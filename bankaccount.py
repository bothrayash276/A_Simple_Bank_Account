import pandas as pd
import random



# Bank Account Number Generator and Transaction ID Generator
def randomGen():
  ran = ""
  for i in range(0,9):
    num = random.randint(1,10)
    ran += str(num)
  return ran




# Opening a New Bank Account
def new_user(name, age, balance):
  
  # Generating Bank Account Number
  bank_number= randomGen()
  
  '''
  0 --> Name
  1 --> Age
  2 --> Bank Balance
  '''

  # Updating New Account Details into Excel File  
  try:
    userExport = pd.read_csv("BankDetails.csv")
  except:
    temp = {
      "acc_num" : ["name", -1, -999]
    }
    fileGeneration = pd.DataFrame(temp)
    fileGeneration.to_csv("BankDetails.csv")
    userExport = pd.read_csv("BankDetails.csv")

  print(f"Your Banking Account Number is {bank_number}")


  userExport[bank_number] = [name,age,balance]
  userExport.to_csv("BankDetails.csv", index=0)


# Creating a Transaction Sheet of Customer
  transData = {
    str(bank_number) : [f"credited {balance}"]
  } 
  file = pd.DataFrame(transData)
  file.to_csv(f"transaction/{bank_number}.csv")






# Updating User Data Base
def update_user_details(bank_number,new_balance):
  user_csv = pd.read_csv(f"BankDetails.csv")
  user_csv.loc[bank_number, "Balance"] = new_balance
  user_csv.to_csv("BankDetails.csv", index=0)





# Displays Customer Bank Balance
def get_balance(bank_number):
    userD = pd.read_csv("BankDetails.csv")
    current_balance = userD.loc[2,bank_number]
    print(f"Your Current Balance is {current_balance}")







# Deposition of Money
def deposit(bank_number, amount):
    userD = pd.read_csv("BankDetails.csv")
    current_balance = int(userD.loc[2,bank_number])

    if(amount>0):
      current_balance += amount
      userD.loc[2,bank_number] = current_balance
      userD.to_csv("BankDetails.csv", index=0)
    else:
      print("Invalid Amount Entered!")






# Withdrawal of Money
def withdraw(bank_number, amount):
    userD = pd.read_csv("BankDetails.csv")
    current_balance = int(userD.loc[2,bank_number])

    if(amount<=current_balance and amount>0):
      current_balance -= amount
      userD.loc[2,bank_number] = current_balance
      userD.to_csv("BankDetails.csv", index=0)
    else:
      print("Invalid Amount Entered")
 





# Updating the Transaction Sheet of User after Transaction
def trans_history(bank_number, choice, amount):
  # date --> Generates a transaction ID for a particular transaction
  date = f"TRN-{bank_number}-"+randomGen()          
  user_trans = pd.read_csv(f"transaction/{bank_number}.csv")
  
  # Getting bank balance
  file = pd.read_csv("BankDetails.csv")
  bank_balance = file.loc[2,bank_number]

  if(choice=='D' and amount>0):
    user_trans[date] = "credited " + str(amount)
  elif(choice=='W' and int(bank_balance)>=int(amount)):
    user_trans[date] = "debited " + str(amount)
  user_trans.to_csv(f"transaction/{bank_number}.csv", index=0)






# Main Function

'''
# D --> Deposit
# W --> Withdraw
# C --> Check balance
# Q --> Quit
'''



print("New User --> N \nExisting User --> E")
user = str(input("User: "))


if(user=='N'):
  # Asking for User Details
  user_name = str(input("Enter your Name: "))
  user_age = int(input("Enter your Age: "))
  user_balance = int(input("Enter your initial balance: "))

  new_user(user_name,user_age,user_balance)
elif(user=='E'):
  accNum = str(input("Enter your Bank Account Number: "))

  print("D --> Deposit \nW --> Withdraw \nC --> Check balance \nQ --> Quit")

  while True:
    
    user_choice = str(input("Choose a option: "))

    # User chose to DEPOSIT
    if(user_choice=='D'):
      user_deposit = int(input("Enter the amount to be deposited: "))
      initial_balance = deposit(accNum,user_deposit)
      trans_history(accNum,user_choice,user_deposit)
      get_balance(accNum)

    # User chose to WITHDRAW
    elif(user_choice=='W'):
      user_withdraw = int(input("Enter the amount to be withdrawn: "))
      initial_balance = withdraw(accNum,user_withdraw)
      trans_history(accNum,user_choice,user_withdraw)
      get_balance(accNum)

    # User chose to CHECK BALANCE
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


