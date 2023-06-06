s="PAYPALISHIRING"
row=5
w=row-3+1
new=""
ind=0
c=0
l=[]
for i in range(len(s)):

    new+=s[i]
    c+=1
    if c==row:
        l.append(new)
        ind+=1
        new=""
    if c==row+w:
        l.append(new.center(row)[::-1])
        ind+=1
        new=""
        c=0
print(ind)
if (ind+1)%2==0:
    l.append((new.ljust(w)).center(row)[::-1])
else:
    l.append(new.ljust(row))
print(l)


new=""
i=0
while len(new)<len(s):
    for ele in l:
        if ele[i]!=" ":
            new+=ele[i]
    i+=1
    
    
print(new)