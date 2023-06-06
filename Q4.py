#Define a function which returns dictionary that stores the words and it's length from the given text
text = "Be happy"
Expected Output: {"Be":2,"happy":5}


text = "Be happy"
text=text.split()
dic={}

for i in text:
    dic[i]=len(i)

print(dic)