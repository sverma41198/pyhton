# Write Python 3 code in this online editor and run it.
s=input("Enter a string:")
m=len(s)//2
new=""

for i in range(len(s)):
    if i<m:
        new=s[i]+new
    elif (i==m):
        new=new+s[m]
    elif len(s)%2==1:
        new=new+s[m-i]
    else:
        new=new[:m]+s[i]+new[m:]

print(new)
    

