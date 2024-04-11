#!/usr/bin/env python
# coding: utf-8

# In[20]:


#subject-->image filter
#using tranformation matrix
#6 functions created
#window created
#6buttons created including functions that are created

def gaussian_blur():
    from PIL import Image, ImageFilter
    import numpy as np
    
    # Open the image
    from tkinter import filedialog
    from PIL import Image, ImageFilter
    image = Image.open(filedialog.askopenfilename())
        
    # Convert PIL image to numpy array (original image)
    original_image_array = np.asarray(image)

    # Apply filter 1 -->gaussian blur
    filtered_image = image.filter(ImageFilter.GaussianBlur())  # Apply blur filter
    # You can apply other filters like ImageFilter.CONTOUR, ImageFilter.EMBOSS, etc.

    # Convert PIL filtered image to numpy array
    filtered_image_array = np.asarray(filtered_image)

    # Save the filtered image
    filtered_image.save('filtered_image.jpg')

    # Show the filtered image
    filtered_image.show()
    
def smooth():
    from PIL import Image, ImageFilter
    import numpy as np
    
    
    # Open the image
    from tkinter import filedialog
    from PIL import Image, ImageFilter
    image = Image.open(filedialog.askopenfilename())

    # Convert PIL image to numpy array (original image)
    original_image_array = np.asarray(image)

    # Apply filter 1 -->smooth
    filtered_image = image.filter(ImageFilter.SMOOTH()) 

    # Convert PIL filtered image to numpy array
    filtered_image_array = np.asarray(filtered_image)

    # Save the filtered image
    filtered_image.save('filtered_image.jpg')

    # Show the filtered image
    filtered_image.show()
    
def edge_enhance():
    from PIL import Image, ImageFilter
    import numpy as np
    
    # Open the image
    from tkinter import filedialog
    from PIL import Image, ImageFilter
    image = Image.open(filedialog.askopenfilename())

    # Convert PIL image to numpy array (original image)
    original_image_array = np.asarray(image)

    # Apply filter 1 --> blur
    filtered_image = image.filter(ImageFilter.EDGE_ENHANCE())

    # Convert PIL filtered image to numpy array
    filtered_image_array = np.asarray(filtered_image)

    # Save the filtered image
    filtered_image.save('filtered_image.jpg')

    # Show the filtered image
    filtered_image.show()
    
def sharpen():
    from PIL import Image, ImageFilter
    import numpy as np
    
    # Open the image
    from tkinter import filedialog
    from PIL import Image, ImageFilter
    image = Image.open(filedialog.askopenfilename())

    # Convert PIL image to numpy array (original image)
    original_image_array = np.asarray(image)

    # Apply filter 1 -->sharpen
    filtered_image = image.filter(ImageFilter.SHARPEN())  
    
    # Convert PIL filtered image to numpy array
    filtered_image_array = np.asarray(filtered_image)

    # Save the filtered image
    filtered_image.save('filtered_image.jpg')

    # Show the filtered image
    filtered_image.show()
    
def emboss():
    from PIL import Image, ImageFilter
    import numpy as np
    
    # Open the image
    from tkinter import filedialog
    from PIL import Image, ImageFilter
    image = Image.open(filedialog.askopenfilename())
    
    # Convert PIL image to numpy array (original image)
    original_image_array = np.asarray(image)

    # Apply filter 1 -->gaussian blur
    filtered_image = image.filter(ImageFilter.EMBOSS())  
    
    # Convert PIL filtered image to numpy array
    filtered_image_array = np.asarray(filtered_image)

    # Save the filtered image
    filtered_image.save('filtered_image.jpg')

    # Show the filtered image
    filtered_image.show()

def unsharp_mask():
    from PIL import Image, ImageFilter
    import numpy as np
    
    # Open the image
    from tkinter import filedialog
    from PIL import Image, ImageFilter
    image = Image.open(filedialog.askopenfilename())
    
    #radius user input
    rad=int(input("Enter radius:"))
    # Convert PIL image to numpy array (original image)
    original_image_array = np.asarray(image)

    # Apply filter 1 -->gaussian blur
    filtered_image = image.filter(ImageFilter.UnsharpMask(radius=rad))  
    
    # Convert PIL filtered image to numpy array
    filtered_image_array = np.asarray(filtered_image)

    # Save the filtered image
    filtered_image.save('filtered_image.jpg')

    # Show the filtered image
    filtered_image.show()

#Output the original and filtered images as numpy arrays
def og_array():
    print("Original Image as NumPy Array:\n", original_image_array)

def filter_array():    
    print("\nFiltered Image as NumPy Array:\n", filtered_image_array)
    
    
#importin the library
import tkinter as tk

#creating a window
window=tk.Tk()

#change window title
window.title('SAFARX')

#size of the window
window.geometry('550x350')

#create head lable for project
tk.Label(window,text='Applied Maths Project',font=('Helvetica',20)).place(x=160,y=10)


#create head lable for creator
tk.Label(window,text='Made by SAFARX',font=('Nyala',8)).place(x=240,y=60)

#button
tk.Button(window,text='Gaussian blur',command=gaussian_blur,width=(17),height=(3)).place(x=30,y=100)  

#button
tk.Button(window,text='Smooth',command=smooth,width=(17),height=(3)).place(x=220,y=100)

#button

tk.Button(window,text='Edge enhance',command=edge_enhance,width=(17),height=(3)).place(x=390,y=100)

#button
tk.Button(window,text='Sharpen',command=sharpen,width=(17),height=(3)).place(x=30,y=190)

#button
tk.Button(window,text='Emboss',command=emboss,width=(17),height=(3)).place(x=220,y=190)

#button
tk.Button(window,text='Unsharp mask',command=unsharp_mask,width=(17),height=(3)).place(x=390,y=190)

#display the window
window.mainloop()


# In[ ]:





# In[ ]:




