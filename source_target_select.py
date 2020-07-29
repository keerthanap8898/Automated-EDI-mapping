#!/usr/bin/env python
# coding: utf-8

# In[9]:


from tkinter.filedialog import askopenfilename
def select_files():
    print("Select the source file from the pop up window\n")
    filename1 = askopenfilename()
    print("Select the destination file from the pop up window\n")
    filename2 = askopenfilename()
    ds=(open(filename1,"r")).readlines()
    dd=(open(filename2,"r")).readlines()
    return(filename1,filename2,ds,dd)


# In[ ]:





# In[ ]:





# In[ ]:




