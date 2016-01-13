__author__ = 'Yilin'
import pandas as pd
import numpy as np
res = pd.read_pickle("data\\file.p")
groups = res.groupby('con_id')
list = []
for group in groups:
    resam = group[1].resample('Min', how = 'last')
    resam = resam.dropna()
    list.append(resam)

res = pd.concat(list, axis = 0)
print res

# grouper = res.groupby([pd.TimeGrouper('1H'), 'con_id'])
# for group in grouper:
#     print group
#     assert False