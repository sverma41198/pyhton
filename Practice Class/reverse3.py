def isVowel(chr):
    return chr in ['A','E','I','O','U']

def reverse(lst):
    new_lst=[]
    for i in lst:
        if len(i)>=5:
            temp=i[::-1]
            newstr=""
            for i in range(len(temp)):
                if not isVowel(temp[i]):
                    newstr+=temp[i]
            new_lst.append(newstr)
        else:
            new_lst.append(i)

    return new_lst

data=["ANDAMAN","GOA","DELHI"]
print(reverse(data))