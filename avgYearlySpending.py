import csv
import numpy as np

with open("customer_spends.csv", "rb") as f:
    reader = csv.reader(f)
    next(f)
    maleSpendList = []
    femaleSpendList = []
    for row in reader:
        name = (row[0])     # Stores value of the first column i.e name in this case
        spend = float(row[1])   # Stores value of the second column i.e their spend in this case
        if "Mr." in name:
            maleSpendList.append(spend)
        elif "Mrs." or "Miss." in name:
            femaleSpendList.append(spend)
    f.close()

print(np.mean(maleSpendList))
print(np.mean(femaleSpendList))
