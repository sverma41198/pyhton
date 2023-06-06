# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def count_digits(n):
    if n<10:
        return 1
    else:
        return 1+count_digits(n//10)
def reverse(x):
    if x<0:
        n=abs(x)
        temp=n
        count=count_digits(n)
    else:
        count=count_digits(x)
        temp=x
    rev=0
    while temp>0:
        d=temp%10
        rev=d*(10**count)+rev
        count-=1
        temp=temp//10
    print(x)
    if rev%10==0:
        rev=rev//10
    if x<0:
        print(int('-'+str(rev)))
    else:
        print(rev)
        
        
reverse(-120)
    
    
    
