# -*- coding: utf-8 -*-
"""
Created on Fri May 13 16:05:36 2016

@author: ajith
"""

import pandas as pd
import pylab as pl
import seaborn as sbn
import numpy as np

#Data directory
data_path = '/Users/ajith/bigdata/data/'

#Open file
excel_val = pd.read_excel(data_path + 'condom_study.xlsx')

fig = pl.figure(1)

ans_len = [3,4,5,2,3,3,3,3,3,3,3,2,2,3,9]

#Explore all the objects and store them in subplots
for ii in range(np.shape(excel_val)[1]):
    ax1 = fig.add_subplot(3,5,ii+1)
    curr_val = excel_val['Q'+str(ii+1)]
    curr_val = curr_val[~np.isnan(curr_val)]
    bin_range = range(1,ans_len[ii]+2)
    ax1.hist(curr_val, bins = bin_range)
    ax1.set_title('Q'+str(ii+1))
    ax1.set_xticks(bin_range[:-1])
    
pl.tight_layout()
pl.savefig('figures/hist_all_qs.pdf', format = 'pdf')    
pl.show()
    
    

