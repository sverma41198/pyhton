
from statistics import median
 
l1=[1,4]
l2=[2,3,7]

l1.extend(l2)
l1=sorted(l1)
med=median(l1)
print(round(float(med),4))