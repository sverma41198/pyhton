#Sort the below list without using inbuilt function I = [2,3,-5,-7,9,4,6,-1,-8,0]
l= [2,3,-5,-7,9,4,6,-1,-8,0]

for i  in  range (len(l)):
    min=i
    for j in range(i+1,len(l)-1):
        if l[j]<l[min]:
            min=j
            
            
    temp=l[min]
    l[min]=l[i]
    l[i]=temp
            
print(l)