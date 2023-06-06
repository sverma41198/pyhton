data=[[1,2,3],[],[],[[]],['a'],['a'],[[],'a'],[[1]]]

def count_empty_list(lst):
    count=0
    for i in lst:
        if i==[] :
            count+=1
        # elif len(i)==1:
        #     if len(i[0])==0:
        #         count+=1
        if i==[[]]:
            count+=1
    return  count

print(count_empty_list(data))