#!/usr/bin/env python
# coding: utf-8

# In[33]:


def area():
    #area of a room
    #length and breadth
    length=float(input('enter the length:'))
    breadth=float(input('enter the breath:'))
    #formula
    area=length*breadth
    #display result
    print('The area of the room is',area,'square feet')

#window
#inport library
import tkinter as tk
#CREATE WINDOW
window=tk.Tk()
#change title 
window.title('area generator')
#change size
window.geometry('300x300')
#label
tk.Label(window,text='area of room',font=('Helvetica',20)).place(x=80,y=10)
#button 
tk.Button(window,text='START',width='20',height='2',command=area).place(x=80,y=145)
#main loop
window.mainloop()


# In[ ]:





# In[ ]:




