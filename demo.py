n=5
width=4*n-3
c=n
str=""
for j in range(width):
    if j<(17//2) and j%2==0:
        str+=chr(96+c)
        c-=1
    elif j<(17//2) and j%2==1:
        str+="-"
    elif j==(17//2) and j%2==0:
        str+=chr(96+c)
    elif j>(17//2) and j%2==0:
        c+=1
        str+=chr(96+c)
    elif j>(17//2) and j%2==1:
        str+="-"

print(str)