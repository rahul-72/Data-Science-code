#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
n,l,h = map(int, input("Enter number of itmes,low value,high value:  ").split(','))
data = [np.random.randint(l,h) for var in range(n)]
k = 1 + 3.322*(np.math.log10(n))
c = (h-l)/k

print()
print()
lcf = 0
mcf = n  

classes = []
for i in range(round(k)):
    cls = (round(l), round(l+c))
    count = 0
    for var in range(round(l), round(l+c)):      
        count+=data.count(var)
    lcf+=count
    classes.append([cls,count,lcf,mcf])
    mcf-=count
    l = l+c

print("Classes \t Frequency \t Less then Cummulative frequency \t More then cummulative frequency") 
print()
t = 0
for key,value,qwe,qaz in classes:
    print(key,'\t',value,'\t\t\t\t',qwe,'\t\t\t\t\t', qaz)
    t+=value
print()  
print()
print("Total number of itmes \t", t)  


# 
