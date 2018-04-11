# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 13:27:20 2018

@author: s2286066
"""
# this the last working comparison of BRRM dataset and Roynat data

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

def remove_out(m,temp):
    k=temp.describe()
    delta=k['75%']-k['25%']
    low=k['25%']-m*delta
    high=k['75%']+m*delta
    short=temp[temp>low][temp<high]
    percent_out=round((len(temp)-len(short))/len(temp)*100,1)
    return short, percent_out

os.chdir('M:\\Data\\IRM\IFRS 9 Proxy Replacement Project\\Roynat Segment\\Data\\BRRM')
m=10  # the number of interquartile ranges used for the detection of outliers

tp_1 = pd.read_csv('dataset_from_Roynat.csv', skipinitialspace=True, encoding="ISO-8859-1" )  
#tp_1.info()
hed1=list(tp_1.columns.values)
#tp_1.describe()
tp_r=tp_1[hed1[4:15]]
tp_r.info()
hed=list(tp_r.columns.values)
#printing histogram for values
for i in range (0,11):
    plt.figure(figsize=(7, 4))
    temp=tp_r[hed[i]][np.isfinite(tp_r[hed[i]])]
    short,percent_out=remove_out(m,temp)
    plt.hist(short, bins=25)
    plt.grid(True)
    plt.legend(loc=0)
    plt.xlabel('value')
    plt.ylabel('frequency')
    plt.title(hed[i]+ ' ,percent removed '+str(percent_out))


#split by year
view1=tp_1.groupby(tp_1[hed1[2]]).Client.nunique()
print (view1)
#breakdown by client type
view2=tp_1.groupby(tp_1[hed1[3]]).Client.nunique()
print (view2)

#   increasing the size by 1,000  to be comparable with BRRM dataset
tp_r[hed[6]]=tp_r[hed[6]]*1000

tp_r[hed[i]]

tp_b = pd.read_csv('BRRM Calibration Data.csv', skipinitialspace=True)  
tp_b.info()
hed_b=list(tp_b.columns.values)
for i in range (0,11):
    plt.figure(figsize=(7, 4))
    #Roynat dataset
    temp=tp_r[hed[i]][np.isfinite(tp_r[hed[i]])] #selecting non-NA values
    leng=len(temp)    
    short_r,percent_out1=remove_out(m,temp)  #remiving outliers and recording the percent of removed values
    # BBRM dataset
    temp=tp_b[hed_b[i]][np.isfinite(tp_b[hed_b[i]])]
    short_b,percent_out2=remove_out(m,temp)
    # selectiog subset of BBRM data with the same length as Roynat
    short_B=np.random.choice(short_b, size=leng, replace=True, p=None)     
    # plot
    fig, ax = plt.subplots(figsize=(7, 4))
    plt.boxplot([short_r,short_B])
    plt.grid(True)
    plt.setp(ax, xticklabels=['Roynat', 'BRRM'])
    plt.xlabel('data set')
    plt.ylabel('value')
    plt.title(hed[i]+ ' ,percent removed '+str(percent_out1)+' and '+str(percent_out2))



