__author__ = 'Yilin'

import pandas as pd
import  numpy as np

def f(x):
    return x['a'] + 1


a = [1, 2 ,3]
b = [4, 5, 6]
s = pd.DataFrame(a, columns = ['a'])
f = pd.DataFrame(a, columns = ['a'])
c = pd.DataFrame(a, columns = ['c'])

k = pd.concat([s, f, c], axis = 1)
print type(k['c'])
# k = s.apply(f, axis = 1)
# re =  k*s
# print re[0]*re[1]




