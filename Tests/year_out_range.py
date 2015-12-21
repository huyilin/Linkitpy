__author__ = 'Yilin'
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pylab as plt
import matplotlib.dates as md


t1 = pd.Timestamp('2015-09-15 01:40:00')
t2 = pd.Timestamp('2015-09-15 03:21:00')

nav = pd.DataFrame({'timestamp' : [t1, t2], 'value' : [1, 2]})
nav = nav.set_index('timestamp')
nav = nav.asfreq('1Min', method = 'pad')

t3 = pd.Timestamp('2015-09-15 03:21:06.126668')
t4 = pd.Timestamp('2015-09-15 03:21:07.126668')
t5 = pd.Timestamp('2015-09-15 03:22:00')

nav2 = pd.DataFrame({'timestamp' : [t3, t4, t5], 'value' : [1, 2, 3]})
nav2 = nav2.set_index('timestamp')
nav = nav.append(nav2)


print nav


xfmt = md.DateFormatter('%Y-%m-%d %H:%M')
ax = nav.plot()

ax.xaxis.set_major_formatter(xfmt)
plt.gcf().autofmt_xdate()
plt.savefig('ok.png')