#!/usr/bin/env python
# coding: utf-8

# $\color{orange}{\text{Third_EXC}}$ 

# In[8]:


def my_sort_Column(x):
    order = np.where([ x[:,1]==np.sort(x[:,1])[i] for i in range(x.shape[1]) ])
    print(x[order[1]])
def my_sort_Row(x):
    order = np.where([ x[1,:]==np.sort(x[1,:])[i] for i in range(x.shape[1]) ])
    print(x[order[1]])


# Test

# In[16]:


import numpy as np
a = np.array([[10, 9, -4, 20], [18, 3, 5, 21], [-4, 0, 10, 11], [15, -2, 10, 1]])

print("a is :\n",a,"\n\n\n")

print("Sort by secound row :\n");my_sort_Row(a)
print("Sort by secound Column :\n");my_sort_Column(a)


# _:)_
