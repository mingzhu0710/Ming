#!/usr/bin/env python
# coding: utf-8

# In[5]:


import  pandas  as pd
import numpy as np
import xlrd
import prettytable as pt

#dealing with nan
infilename = r'dataset.xlsx'
workbook = xlrd.open_workbook(infilename)
df = workbook.sheet_by_name('dataset1')
num_rows = df.nrows   
num_cols = df.ncols
t = 0
im_data = np.zeros((num_rows, num_cols))
for curr_row in range(num_rows):    
    for curr_col in range(num_cols):        
        rawVal = df.cell(curr_row, curr_col).value        
        if isinstance(rawVal, str):            
            im_data[curr_row, curr_col] = np.nan        
        else:            
            im_data[curr_row, curr_col] = float(rawVal)
print(im_data)

month_end = []

for i in range(num_rows):
    if im_data[i][1] < 20150401.0 and im_data[i+1][1] >= 20150401.0:
        month_end.append(i)
    if im_data[i][1] == 20150430.0:
        month_end.append(i)
print(month_end)
result = [[0 for j in range(1,4)]for i in range(1,5)]
for i in range(len(month_end)):
    j = month_end[i]
    for m in range(j,-1,-1):
        if im_data[m][2] == 'nan' and 0 < im_data[m][1] - im_data[m-1][1] < 50 :
            pass
        else:
            m -= 1
            break
    result[i][0] = im_data[m][0]
    result[i][1] = im_data[m][1]
    result[i][2] = im_data[m][2]
    
print(result)

 
#plot
tb = pt.PrettyTable()
tb.field_names = ["ID", "trading_date", "mktvalue"]
tb.add_row(result[0])
tb.add_row(result[1])
tb.add_row(result[2])
tb.add_row(result[3])
 
print(tb)

