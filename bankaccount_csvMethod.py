import random
import csv
import os
import datetime

fieldName = ["acc_number","full_name", "age", "balance"]

# Bank Account Number Generator
def bank_number_gen():
    bng = ""
    for i in range(0,10):
       num = str(random.randint(1,9))
       bng += num
    return bng





# Printing Bank Balance
def get_balance(bank_number):
   with open("bank_details.csv", 'r') as file:
      csv_reader = csv.DictReader(file, fieldnames=fieldName)
      for line in csv_reader:
         if(line["acc_number"]==str(bank_number)):
            print("Current Balance - ", line["balance"])
            return int(line["balance"])





# Function to update the bank balance of customer (sub-function)
def csv_updater(account_number, balance):
   with open("bank_details.csv", 'r') as file:
      csv_reader = csv.DictReader(file, fieldnames=fieldName)
      with open("disposable.csv", 'w') as dFile:
         csv_writer = csv.DictWriter(dFile, fieldnames=fieldName)
         # csv_writer.writeheader()
         for entry in csv_reader:
            if(entry['acc_number']!=str(account_number)):
               csv_writer(entry)
            else:
               userD = {
                  "acc_number" : entry["acc_number"],
                  "full_name" : entry["full_name"],
                  "age" : entry["age"],
                  "balance" : balance
               }
               csv_writer.writerow(userD)
   # getRid(account_number)


# Renaming the CSV File
def getRid(bn):
   os.remove("bank_details.csv")
   os.rename("disposable.csv", "bank_details.csv")
   print("Transaction Successful!")
   get_balance(bn)
   print()




# Transaction LOG System
def transaction_log(user,bank_number, amount):
   current_date = str(datetime.datetime.now())
   trans_header = ["date", "status", "amount"]
   if(user=="D"):
      with open(f"transactions/{bank_number}.csv", 'a') as file:
         csv_writer = csv.DictWriter(file, fieldnames=trans_header)
         transaction = {
            "date" : current_date,
            "status" : "CREDITED",
            "amount" : amount
         }
         csv_writer.writerow(transaction)

   elif(user=="W"):
      with open(f"transactions/{bank_number}.csv", 'a') as file:
         csv_writer = csv.DictWriter(file, fieldnames=trans_header)
         transaction = {
            "date" : current_date,
            "status" : "DEBITED",
            "amount" : amount
         }
         csv_writer.writerow(transaction)


# System to create a new user profile
def new_user(name, age, balance):
    acc_number = bank_number_gen()
    with open("bank_details.csv", 'a') as bd_file:
      csv_writer = csv.DictWriter(bd_file, fieldnames=fieldName)
      # csv_writer.writeheader()
      detailList = {
         "acc_number" : acc_number,
         "full_name" : name,
         "age" : age,
         "balance" : balance
      }
      csv_writer.writerow(detailList)
      print(acc_number)
      

def deposit(bank_number, amount):
   if(amount > 0):
      with open("bank_details.csv", 'r') as file:
         csv_reader = csv.DictReader(file,fieldnames=fieldName)
         for line in csv_reader:
            if(line["acc_number"]==str(bank_number)):
               bank_balance = int(line["balance"])    
               bank_balance += amount
               csv_updater(bank_number,bank_balance)
               transaction_log("D", bank_number, amount)
            else:
               pass
      getRid(bank_number)
   else:
      print("Invalid Amount Entered!")

def withdraw(bank_number, amount):
   
   if(int(get_balance(bank_number))>=amount and amount > 0):
      with open("bank_details.csv", 'r') as file:
         csv_reader = csv.DictReader(file, fieldnames=fieldName)

         for line in csv_reader:
            if(line["acc_number"]==str(bank_number)):
               bank_balance = int(line["balance"])
               bank_balance -= amount
               csv_updater(bank_number,bank_balance)
               transaction_log("W", bank_number, amount)
            else:
               pass
      getRid(bank_number)
   else:
      print("Invalid Amount Entered!")








# Main Code

print("New User --> N \nExsiting User --> E")
system_entry = input("Enter - ")
if(system_entry=="N"):
   name = input("Enter your Name - ")
   age = int(input("Enter your age - "))
   initial_deposit = int(input("Enter your initial deposit amount - "))
   new_user(name,age,initial_deposit)
elif(system_entry=="E"):
   accNum = int(input("Enter your account number - "))
   print("Deposit --> D \nWithdraw --> W \nCurrent Balance --> C \nQuit --> Q\n")
   while (True):
      loop_entry = input("Enter - ")
      if(loop_entry=="D"):
         depo = int(input("Enter the amount to be deposited - "))
         deposit(accNum, depo)
         # getRid(accNum)
      elif(loop_entry=="W"):
         witdr = int(input("Enter the amount you want to withdraw - "))
         withdraw(accNum, witdr)
         # getRid(accNum)
      elif(loop_entry=="C"):
         get_balance(accNum)
      elif(loop_entry=="Q"):
         break
      else:
         print("Invalid Response")
      #Clear The Line
      print("")



