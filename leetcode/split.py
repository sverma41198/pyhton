str="GFGaBstuforigeeks"
new_lst=[]
c=0
new=""
for i in range(c,len(str)):
    if i==len(str)-1:
        new_lst.append(str[c:len(str)])
    if str[i] in ("aeiou"):
        new=str[c:i]
        if new!="":
            new_lst.append(new)
        c=i+1
        
print(new_lst)


               