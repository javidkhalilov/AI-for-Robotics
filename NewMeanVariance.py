# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 23:41:16 2016

@author: Javid
"""

import math

def update(mean1, var1, mean2, var2):
    new_mean =(mean1*var2+mean2*var1)/(var1+var2)
    new_var =1/(1/var1+1/var2)
    return [new_mean, new_var]
    
def predict(mean1, var1, mean2, var2):
    new_mean =mean1+mean2
    new_var =var1+var2
    return [new_mean, new_var]

print (predict(10., 4., 12., 4.))    
    
    
print (update(10.,8.,13., 2.))