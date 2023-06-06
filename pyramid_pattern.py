depth=int(input("Enter Depth:"))
w=depth+depth-1
counter=1
for i in range(depth):
    width=i+counter
    str=""
    for j in range(width):
        if j==0 or j==width-1:
            str+="*"
        else:
            str+="_"
    print(str.center(w))
    counter+=1