#Given a string "abcde", Display the output as "a1b2c3d4e5"

string="abcde"
newstr=""
for i in range(len(string)):
    newstr+=string[i]+str(i+1)
print(newstr)