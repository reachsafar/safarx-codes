#!/usr/bin/env python
# coding: utf-8

# In[2]:


#welcome user
print('!!!Welcome to SAFARX Head N Tails!!!')

#ask its choice
u_choice=input('What do you chooose?').title()

#print its choice
print('Your choice is...',u_choice)

#coin toss
import random
if random.choice('ht')=='h':
    coin_toss='Head'
else:
    coin_toss='Tail'

    #display coin toss result
print('Coin tossed and its...',coin_toss)

#if matched-->you won
if coin_toss.title()==u_choice.title():
    print('Damn boy!!You nailed it.')
#else-->lost
else:
    print('Oops!Try again later.')

    #thankyou
print('Thankyou!Visit again.')


# In[ ]:




