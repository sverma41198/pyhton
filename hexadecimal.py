
n=1615
factors=[]
while n>0:
    d=n%16
    if d>9:
        d=chr(64+d-9)
    factors.append(str(d))
    n=n//16
print("".join(factors[::-1]))