__author__ = 'Yilin'
import pandas as pd
import matplotlib.pyplot as plt

################################################
# data
t1 = pd.to_datetime('2012-01-01 00:00:00')
t2 = pd.to_datetime('2012-01-02 00:00:00')
t3 = pd.to_datetime('2012-01-03 00:00:00')
t4 = pd.to_datetime('2012-01-04 00:00:00')
t5 = pd.to_datetime('2012-01-05 00:00:00')
t6 = pd.to_datetime('2012-01-06 00:00:00')
t7 = pd.to_datetime('2012-01-07 00:00:00')

################################################
# concat and fillna

frame1 = pd.DataFrame([1, 2, 3], index = [t2, t1, t3], columns = ['well'])
frame2 = pd.DataFrame([3, 4, 5, 6], index = [t1, t2, t3, t4], columns = ['fine'])

frame = pd.concat([frame1, frame2])
print frame.fillna(method = 'pad')

################################################
# sort by index
print
frame1 = frame1.sort_index(axis=0)

################################################
# The draw style

# frame1.plot(drawstyle = 'steps-post')
# plt.show()

################################################
#the dict

frame = pd.DataFrame({'data' : [1,2,3,4,5,6,7,8, 9], 'ib_code' : ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'c'], 'time' : [t1, t2, t3, t4, t5, t6, t7, t7, t7]})
frame = frame.set_index('time')
f = frame.groupby('ib_code')
print frame
prices = pd.DataFrame({a: b['data'] for a, b in f})
print prices

#################################################
# disable the auto scaling
ax = frame.plot()
ax.set_autoscaley_on(False)

