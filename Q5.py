
'''Let's consider there is a list which contains usernames, You have received requirement to add one more username to the list (without using append and assignment approaches)

input: ["user1","user2"]
output: ["user1","user2","user3"]'''

l=["user1","user2"]
new=input("Enter new user:")
l.insert(len(l),new)
print(l)