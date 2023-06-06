data={'A':['Apple','Ant'],'B':['Banana','Bat'],'C':['Citrus','Cat']}
data2={}
for i in data:
    for j in data[i]:
        data2[j]=i
print(data2)


