def check_string(l):
    count=0
    for i in lst:
        if type(i)==str:
            count+=1
    return count    

#list to store values of different type
lst=[1,'23 ',5,'Rahul','XYZ']
print(check_string(l))