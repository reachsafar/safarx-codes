#!/usr/bin/env python
# coding: utf-8

# **password generator**
# 

# In[17]:


#welcome user
import random
import string

#define length
length=int(input('Enter the length of password:'))

#all character
all_characters=string.ascii_letters+string.digits+string.punctuation


#if length less than 8-->need more characters to generate pass word 
if length<8:
    print('Increase the length of password to generate password!!')
else:
    for i in range(length):
        password=(random.choice(all_characters))
        print(password,end='')


# **password generator 2**

# In[27]:


#welcome user
import random
import string

#define length
length=int(input('Enter the length of password:'))

#all character
all_characters=string.ascii_letters+string.digits+string.punctuation
password=''

#if length less than 8-->need more characters to generate pass word 
if length<8:
    print('Increase the length of password to generate password!!')
else:
    for i in range(length):
        password=password+(random.choice(all_characters))
    print(password)


# In[ ]:




