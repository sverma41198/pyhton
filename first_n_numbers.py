
n=10000
for i in range(1,n+1):
    sum=(i*(i+1))//2
    for j in range(1,i+1):
        if sum==j**2:
            print(i)