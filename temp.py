import csv
f = ["acc_number", "full_name", "age", "balance"]
with open("bank_details.csv", 'r') as file:
    csv_reader = csv.DictReader(file, fieldnames=f)
    for line in csv_reader:
        if(line["full_name"]=="Yash Bothra"):
            print(type(line["balance"]))