import math


#print(dir(math))

def calculatePosition(*position):
    if position[1]=='U':
        position[0][0]+=position[2]
    elif position[1]=='D':
        position[0][1] += position[2]
    elif position[1]=='L':
         position[0][2] += position[2]
    else:
        position[0][3] += position[2]

        return position[0]

current1 = [0,0,0,0]
calculatePosition(current1,'U',5)
calculatePosition(current1,'D',3)
calculatePosition(current1,'L',3)
calculatePosition(current1,'R',2)

print("Final Position: (", (current1[0]-current1[1]),",", (current1[3]-current1[2]) , ")")