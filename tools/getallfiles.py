__author__ = 'Yilin'
"""
    To get all the files under a directory
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

direc =  os.getcwd()
direc = direc.split("\\")
direc[-1] = 'data'
path = '\\'.join(direc) + '\\pnl7.pk'
frame = pd.read_pickle(path)
frame2 = frame.diff()
frame3 = frame2.groupby(pd.TimeGrouper(freq= '1D')).aggregate(np.sum)
frame3.to_clipboard()

