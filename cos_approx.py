#!/usr/bin/env python
# coding: utf-8

# In[37]:


import math

x = float(input("Please enter the number you want to find its cosine value."))

i = 1
cos_x = 1

while i <= 12:
    cos_x = cos_x + ((-1)**i) * (x**(2*i)) / math.factorial(2*i)
    i = i + 1
    
print("cos(%f) approximation is %.16f" %(x,cos_x))

