import matplotlib.pyplot as p
import csv,numpy as np

list_hurricanes = list()
list_year = list()
with open("../data/Hurricanes.csv", mode="r") as h:
    reader = csv.DictReader(h)
    for row in reader:
        print(row)
        list_hurricanes.append(row.get("Hurricanes"))
        list_year.append(row.get("Year"))

print("list_hurricanes == \n",list_hurricanes)
print("list_year == \n",list_year)
x_axis = np.asarray(list_year,dtype=int)
y_axis = np.asarray(list_hurricanes,dtype=int)
p.bar(x_axis,y_axis, alpha=0.8,align='center')
print(type(p))
p.title("Hurricanes Summary")
p.grid(True)
p.xlabel("Year")
p.ylabel("Number Of HurriCanes")
p.show()
