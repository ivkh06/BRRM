# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 13:27:20 2018

@author: s2286066
"""

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
m=10
def remove_out(m,temp):
    k=temp.describe()
    delta=k['75%']-k['25%']
    low=k['25%']-m*delta
    high=k['75%']+m*delta
    short=temp[temp>low][temp<high]
    percent_out=round((len(temp)-len(short))/len(temp)*100,1)
    return short, percent_out

os.chdir('M:\\Data\\IRM\IFRS 9 Proxy Replacement Project\\Roynat Segment\\Data\\BRRM')

#fields=read_header(dirname+name)

tp_b = pd.read_csv('BRRM Calibration Data.csv', skipinitialspace=True)  
tp.info()
tp.describe()
hed=list(tp.columns.values)
#printing histogram for values
for i in range (0,11):
    plt.figure(figsize=(7, 4))
    temp=tp[hed[i]][np.isfinite(tp[hed[i]])]
    short,percent_out=remove_out(m,temp)
    plt.hist(short, bins=25)
    plt.grid(True)
    plt.legend(loc=0)
    plt.xlabel('value')
    plt.ylabel('frequency')
    plt.title(hed[i]+ ' ,percent removed '+str(percent_out))


tp[hed[2:4]]
tp[hed[2:4]].info()

leng=[len(a) for a in (tp[hed[2:3]])]

tp[hed[4]].head(10)

#split by year
view1=tp.groupby(tp[hed[2]]).Client.nunique()

#breakdown by client type
view1=tp.groupby(tp[hed[3]]).Client.nunique()

#breakdown by client type
view1=tp[tp[hed[4]]!='NA'].groupby(tp[hed[4]]).Client.nunique()



plt.hist(short, bins=20)

hed[i]

sorted(temp)[5:10]
min (temp)
