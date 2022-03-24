# -*- coding: utf-8 -*-
"""
df_utils
utilities for working with dataframes
R vector replications and some syntactic sugar
Created on Fri Mar 11 15:36:49 2022

@author: shorowitz
"""

import pandas as pd
import numpy as np

def cat_bin(input_vec, f_bins, f_names, do_abs=False):
    # to do - add f_names=auto (alpha vector),
    # f_names=char (str version of numvec)
    # percentiles as name bins (maybe as standalone func?)
    # n even spaced bins
    # error handling for incorrect f_names / bins length
    
    if f_bins[0]!=-np.inf:
        f_bins.insert(0, -np.inf)
        
    if f_bins[-1]!=np.inf:
        f_bins.append(np.inf)
        
    print(f_bins)
    
    if do_abs:
        int_vec = list(map(abs, input_vec))
    else:
        int_vec = input_vec
    output_vec = list(pd.cut(int_vec, bins=f_bins, labels=f_names))
    print("printing nowt")
    return(output_vec)

def perc_bin(input_vec, perc_bins=[0,0.25,0.50,0.75,1.0]):
    print("perc_bin not defined yet")
    