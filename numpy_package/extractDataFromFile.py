import csv,numpy as np

arr = []
male,female=0,0
with open("../data/SalaryGender.csv", mode="r") as cf :
    csv_reader = csv.DictReader(cf)
    for row in csv_reader:
        temp = []
        temp.append(row)
        arr.append(temp)
        if row.get('PhD') == "1" and row.get('Gender') == "1":
            male +=1
        elif row.get('PhD') == "1" and row.get('Gender') == "0":
            female+=1

print("Male with PhD : ", male)
print("FeMale with PhD : ", female)
print("Total number of PHD members : ", (female+male))


np.save("../data/ExtractDataResult.npy", arr)
data = np.load("../data/ExtractDataResult.npy", allow_pickle=True)
print("Numpy Loaded Data ===" , data)
