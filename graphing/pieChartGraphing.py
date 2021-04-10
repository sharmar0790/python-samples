import csv,numpy as np
import matplotlib.pyplot as p

pieDict = {}
with open("./data/Cars2015.csv", mode="r") as cf :
    csv_reader = csv.DictReader(cf)
    for row in csv_reader:
        if row.get("Make").strip() in pieDict:
            pieDict[row.get("Make").strip()] = pieDict.get(row.get("Make").strip())+1
        else:
            pieDict[row.get("Make").strip()]=1

#print(pieDict)

labels = list(pieDict.keys())
sizes = list(pieDict.values())
p.pie(sizes, labels=labels)
p.show()
