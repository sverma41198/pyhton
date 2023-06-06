#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(list(matrix_item))
s="" 
for i in range(m):
    for j in range(n):
        s=s+matrix[j][i]
i=0
c=0
newstr=""
special=""
while  i<len(s):
    while i<len(s) and s[i].isalpha():
        newstr=newstr+s[i]
        i+=1
    special=""
    while i<len(s) and not s[i].isalpha() :
        special+=s[i]
        i+=1
    newstr+=" "
    while i<len(s) and not s[c].isalpha() and s[i].isalpha():
        newstr=newstr+special
        c=i
print(newstr.strip()+special)