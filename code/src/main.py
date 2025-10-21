#!/usr/bin/env python

from tkinter.filedialog import askopenfilename
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 
from code import source_target_select as sts
from code import extract_details as ed
from code import ruleset_generation as rg




filename1,filename2,ds,dd=sts.select_files()

## OUTPUT 1: (pop up window)
"""
-> Select the source file from the pop up window.
-> Select the destination file from the pop up window.
"""
#--------------------------------------------------------------------------------------------------------------------------


path,pack,source,dest,so,de=ed.extract_attr(filename1,filename2,ds,dd)

dicts=ed.extract_source_attr(ds)
dictd=ed.extract_dest_attr(dd)

## OUTPUT 2:
"""
C:/Users/kp/workspace/com.extol.ebi.demo01.singlefftoff/src/com/extol/ebi/demo01/singlefftoff
com.extol.ebi.demo01.singlefftoff
DelimitedFF
FixedFF
Source
Target
{'FirstName': 'String', 'LastName': 'String', 'Quantity': 'Integer', 'Color': 'String', 'UnitPrice': 'Decimal'}
{'FullName': 'String', 'TotalPrice': 'Decimal', 'ColorCode': 'String', 'Units': 'Integer'}
"""
#--------------------------------------------------------------------------------------------------------------------------


finalmap=rg.predict_map(dicts,dictd)
RSpath=rg.generate_RS(path,pack,source,dest,so,de,finalmap)

## OUTPUT 3: Final Result
"""
{'FullName': ['FirstName', 'LastName'], 'TotalPrice': ['UnitPrice'], 'ColorCode': ['Color'], 'Units': ['Quantity', 'UnitPrice']}
The ruleset file has been generated in:
C:\\Users\\kp\\workspace\\com.extol.ebi.demo01.singlefftoff\\src\\com\\extol\\ebi\\demo01\\singlefftoff\\DelimitedFFtoFixedFFRS.ruleset
"""
#--------------------------------------------------------------------------------------------------------------------------
