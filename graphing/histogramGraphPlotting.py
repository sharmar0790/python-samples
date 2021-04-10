import matplotlib.pyplot as p
import csv,numpy as np

list_2014 = list()
list_Moscow = list()
list_Melbourne = list()
list_sf = list()

list_Moscow_2015 = list()
list_Melbourne_2015 = list()
list_sf_2015 = list()

with open("../data/CityTemps.csv", mode="r") as h:
    reader = csv.DictReader(h)
    for row in reader:
        if row.get("Year") == "2014":
            list_sf.append(row.get("San Francisco"))
            list_Moscow.append(row.get("Moscow"))
            list_Melbourne.append(row.get("Melbourne"))
        else:
            list_sf_2015.append(row.get("San Francisco"))
            list_Moscow_2015.append(row.get("Moscow"))
            list_Melbourne_2015.append(row.get("Melbourne"))

x_axis_sf = np.asarray(list_sf,dtype=float)
x_axis_me = np.asarray(list_Melbourne,dtype=float)
x_axis_mo = np.asarray(list_Moscow,dtype=float)
x_axis_sf_2015 = np.asarray(list_sf_2015,dtype=float)
x_axis_me_2015 = np.asarray(list_Melbourne_2015,dtype=float)
x_axis_mo_2015 = np.asarray(list_Moscow_2015,dtype=float)
#y_axis = np.asarray(list_hurricanes,dtype=int)
#print(x_axis_sf)
#print(x_axis_m)
#p.hist(x_axis_sf,bins=5,alpha=1,label="San Francisco")
#p.hist(x_axis_me,bins=5,alpha=1,label="Melbourne")
#p.hist(x_axis_mo,bins=5,alpha=1,label="Moscow")
#another way
p.hist([x_axis_mo,x_axis_me,x_axis_sf,x_axis_mo_2015,x_axis_me_2015,x_axis_sf_2015],bins=6,alpha=0.9,label=["Moscow","Melbourne","San Francisco","Moscow_2015","Melbourne_2015","San Francisco_2015"])

#p.hist([x_axis_mo_2015,x_axis_me_2015,x_axis_sf_2015],bins=6,alpha=1,label=["Moscow_2015","Melbourne_2015","San Francisco_2015"])
#p.figure(figsize=[10,8])
p.legend(loc= "Upper Right")
p.title("City Temps")
p.grid(True)
p.xlabel("Temperature")
p.ylabel("Bins")
p.xticks(fontsize=15)
p.yticks(fontsize=15)
p.show()
