import numpy as np
from matplotlib import pyplot as plt

hours_x=[0,1,2,3,4,5,6]
f_count_y=[100,200,400,50,18,19,17]
s_count_y=[10,20,40,5,1,9,7]
x_indexes=np.arange(len(hours_x))
width=.25
echo "capture changes"
plt.style.use('fivethirtyeight')
#plt.plot(hours_x,f_count_y, label='count on first day');
#plt.plot(hours_x,s_count_y, label='count on second day');

plt.bar(x_indexes,f_count_y, width=width,label='count on first day');
plt.bar(x_indexes-width,s_count_y, width=width,label='count on second day');

plt.title("hourly count")
plt.xlabel("hours")
plt.ylabel("count of records")




plt.legend();
plt.grid(True);
plt.savefig('matplot.png')
plt.show();
