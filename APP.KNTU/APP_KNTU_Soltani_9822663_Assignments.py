#!/usr/bin/env python
# coding: utf-8

# <img align="right" src="./pic.JPG"     style=" width:180px; padding: 10px; " > 
# 
# # $\color{Blue}{\text{Advance Programming Python}}$
# ## $\color{brown}{\text{K.N.Toosi University of technology}}$
# ## $\color{brown}{\text{Mohammad Javad Soltani 9822663}}$
# 

# ___

# >**- [ 1. First Assignment ](#1)**  
# 
# 

# ___

# # $\color{blue}{\text{First_Assignments}}$ 
# <a name="1"></a>

# $\color{orange}{\text{First_EXC}}$ 

# In[112]:


def reverse(x):
    num = int(x)
    a = num%-10
    num/=10
    num = int(num)
    b = num%-10
    num/=10
    num = int(num)
    c = num%-10
    print(a*100+b*10+c)


# In[114]:


reverse(-345)


# $\color{orange}{\text{Secound_EXC}}$ 

# In[159]:


my_dict = {'a':1, 'b':2, 'c':3, 'd':4}
key_list = ['a', 'b']

def searcher():
    dict_k ={}
    for i in range(len(key_list)):
        if key_list[i] in my_dict.keys():
            dict_k[key_list[i]] = 1 


# In[160]:


searcher()
dict_k


# _:)_
