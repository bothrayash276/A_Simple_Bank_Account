import random
import csv

def bank_number_gen():
    bng = ""
    num = str(random.randint(1,9))
    bng += num
    return bng


def new_user(name, age, balance):
    acc_number = bank_number_gen()
    fieldName = ["acc_number","full_name", "age", "balance"]
    with open("bank_details.csv", 'a') as bd_file:
      csv_writer = csv.DictWriter(bd_file, fieldnames=fieldName)
      csv_writer.writeheader()
      detailList = [acc_number,name,age,balance]
      csv_writer.writerow(detailList)

def deposit(bank_number, amount):
   if(amount > 0):
      with open("bank_details.csv", 'r') as dep_file:
         fieldName = ["balance"]
         csv_reader = csv.DictReader(dep_file, fieldnames=fieldName)
         bank_balance = csv_reader["balance"]
         with open("bank_details.csv", 'a') as dep_file:
         
   else:
      print("Invalid Amount Entered!")



