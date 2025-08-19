import pandas as pd
# file = pd.read_excel("ExcelFile.xlsx", sheet_name="she1", index=False)

file = pd.read_csv("BankDetails.csv")
t  = file.loc[2,"259"]
print(t)