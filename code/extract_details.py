#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def extract_attr(filename1,filename2,ds,dd):
    #SOURCE AND DESTINATION DATA FILENAME ONLY
    slash=filename1.rfind("/")
    dot=filename1.rfind(".")
    source=filename1[(slash+1):dot]
    slash=filename2.rfind("/")
    dot=filename2.rfind(".")
    dest=filename2[(slash+1):dot]
    #PACKAGE NAME
    pack=dd[0].split(" ")
    pack=pack[1]
    #SOURCE AND TARGET FUNCTION NAMES
    for line in ds:
        if "[]" in line:
            so=line.split(" ")
            so=so[len(so)-2]
    for line in dd:
        if "[]" in line:
            de=line.split(" ")
            de=de[len(de)-2]
    #FIND PATH OF THE SOURCE AND DESTINATION FILES TO PUT THE RULESET IN THE SAME FOLDER
    path=filename2[:slash]
    #PRINT VALUES
    print(path+"\n"+pack+"\n"+source+"\n"+dest+"\n"+so+"\n"+de)
    path=path.replace("/","\\\\")
    return(path,pack,source,dest,so,de)


# In[ ]:


def extract_source_attr(ds):
    l1=l2=[]
    dicts={}#SOURCE NODE ATTRIBUTES AND THEIR TYPES
    cond=0
    stringToMatch="def record Source {"
    for line in ds:
        #print(line)
        if stringToMatch in line:
            cond=1
            continue
        if(line!="\t\t}" and cond==1):
            if line == '\n':
                continue
            if '}'in line:
                continue
            else:
                l1=list((line.strip("\t\n")).split(" "))
                l2.append(l1[0])
                dicts[l1[0]]=l1[1]
        elif(line=="\t\t}"):
            cond=0
            break
    print(dicts)
    return(dicts)


# In[ ]:


def extract_dest_attr(dd):
    ll1=ll2=[]
    dictd={}#DESTINATION NODE ATTRIBUTES AND THEIR TYPES
    cond=0
    #stringToMatch="def record Source {"
    for line in dd:
        #print(line)
        if "(" in line:
                ll1=list((line.strip("\t")).split(" "))
                ll2.append(ll1[0])
                dictd[ll1[0]]=ll1[1]
    print (dictd)
    return(dictd)


# In[ ]:



    

