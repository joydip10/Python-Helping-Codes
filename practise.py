import numpy as np


alphabets="abcdefghijklmnopqrstuvwxyz"
my_dict={}
for i in alphabets:
    my_dict[i]=0

l=['hello','world']
for i in l:
    for j in i:
        my_dict[j]=my_dict[j]+1
    
m-0 
for k,v in my_dict.items():
    if v > m:
        m=v
        key=k
        val=v
    

print(key)
print(val)