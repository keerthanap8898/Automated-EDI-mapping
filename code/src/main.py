#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter.filedialog import askopenfilename
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 
from code import source_target_select as sts
from code import extract_details as ed
from code import ruleset_generation as rg


# In[2]:


filename1,filename2,ds,dd=sts.select_files()


# In[3]:


path,pack,source,dest,so,de=ed.extract_attr(filename1,filename2,ds,dd)
dicts=ed.extract_source_attr(ds)
dictd=ed.extract_dest_attr(dd)


# In[4]:


finalmap=rg.predict_map(dicts,dictd)
RSpath=rg.generate_RS(path,pack,source,dest,so,de,finalmap)


# In[ ]:




