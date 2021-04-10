import pandas as pd

ddf = pd.read_csv("../data/DSScoreTerm1.csv")
mdf = pd.read_csv("../data/MathScoreTerm1.csv")
pdf = pd.read_csv("../data/PhysicsScoreTerm1.csv")
#print(df)

ddf1 = ddf.drop(["Ethinicity",'Name'],axis=1)
pdf1 = pdf.drop(["Ethinicity",'Name'],axis=1)
mdf1 = mdf.drop(["Ethinicity",'Name'],axis=1)

#print("Physics == " , pdf1)
#print("Maths === ", mdf1)
#print("DS ==== ", ddf1)

final = ddf1.append(mdf1).append(pdf1,ignore_index=True).fillna(0)
final.loc[final.Sex == "M","Sex"]="1"
final.loc[final.Sex == "F","Sex"]="2"
print(final)


final.to_csv("../data/ScoreFinal.csv",index=False)
