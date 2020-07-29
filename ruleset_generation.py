#!/usr/bin/env python
# coding: utf-8

# In[4]:


from fuzzywuzzy import fuzz 
from fuzzywuzzy import process
def predict_map(dicts,dictd):
    final={}#MAPPING DICTIONARY USING THE FUZZYWUZZY LIBRARY
    for key,value in dictd.items():
        final[key]=[]

    for key,value in dicts.items():
        for key1,value1 in dictd.items():
            fuzzscore=fuzz.WRatio(key,key1)
            if (fuzzscore>55 ):
                final[key1].append(key)
                #print("fuzzy score for the following two is "+key+" "+key1+" "+str(fuzzscore))
    print(final)
    return(final)
    


# In[6]:


def generate_RS(path,pack,source,dest,so,de,final):
    d1=(open("text1.txt","+r")).read()
    d2=(open("text2.txt","+r")).read()
    #print(d1)
    #print(d2)
    filename=path+"\\\\"+source+"to"+dest+"RS.ruleset"
    #print(filename)
    f=open(filename,"w+")
    f.write("package "+pack+"\n\ndef ruleSet "+source+"to"+dest+"RS"+d1+pack+"."+source+"), sourceNode)\n\t\tvar target = bindOutput(typeof("+pack+"."+dest+d2+so+" initNew target._Target {\n")
    move="\n\t\t\tnew Move().execute(source._"+so+".current."
    arrow=") --> #[target._"+de+".current."
    for key in final:
        for val in final[key]:
            f.write(move+val+arrow+key+"]")
    f.write("\n\t\t\t}\n\t\t}\n\t}")
    f.close()
    print("The ruleset file has been generated in:\n"+filename)
    return(filename)


# In[ ]:




