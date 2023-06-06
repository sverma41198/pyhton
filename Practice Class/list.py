data1=[1,5,9,4,0,5]
data2=(9,5,4,1,5,6)

def common_element(data1,data2):
    intersection=[]
    for ele in data1:
        if ele in data2:
            intersection.append(ele)
    return  intersection

print(list(set(common_element(data1,data2))))

def data_unique(data1,data2):
    unique=[]
    for i in data1:
        if i not in data2:
            unique.append(i)
    return unique


print("Unique elements of data1 :",data1_unique(data1,data2))

