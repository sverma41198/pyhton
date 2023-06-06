data1=[1,5,9,4,0,5]
data2=(9,5,4,1,5,6)
data1=set(data1)
data2=set(data2)
z=data1.intersection(data2)
print(z)
# print(data1.adjoint)
print(data1.difference(data2))
print(data2.difference(data1))