import pandas as pd
def func(name,age,number):
    file = pd.DataFrame(
        {
            "15654321" : [name, age,number]
        }
    )
    file.to_csv("transaction/15654321.csv")

# func("yash",18,1235)

fi = "yassbothra"
t = str(fi)
print(t)