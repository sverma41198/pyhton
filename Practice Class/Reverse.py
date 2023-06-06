def reverse(lst):
    new_lst=[]
    for i in lst:
        if len(i)>=5:
            temp=i[::-1]
            new_lst.append(temp)
        else:
            new_lst.append(i)

    return new_lst

data=["ANDAMAN","GOA","DELHI"]
print(reverse(data))


