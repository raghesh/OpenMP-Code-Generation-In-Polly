#/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 8
ind = np.arange(N)  # the x locations for the groups
width = 0.15       # the width of the bars
fig = plt.figure()
ax = fig.add_subplot(111)

gcc = (3.223501, 0.723425, 0.451803, 0.447007, 0.730774, 1.759291, 0.224991, 0.417174)
rects1 = ax.bar(ind, gcc, width, color='red') 

graphite = (3.228089, 0.487649, 0.445492, 0.441063, 0.530774, 1.666291, 0.262309, 0.421496)
rects2 = ax.bar(ind+width, graphite, width, color='black')

polly = (2.472263, 1.024179, 0.249978, 0.263240, 0.444576, 1.022302, 0.275020, 0.591673)
rects3 = ax.bar(ind+2*width, polly, width, color='blue')

# add some
ax.set_ylabel('Runtime')
ax.set_title('Polybench results(2 Core 32bit)')
ax.set_xticks(ind+width/2.0)
ax.set_xticklabels( ('2mm', 'adi', 'correlation', 'covariance', 'doitgen', 
		     'gemm', 'jacobi-2d-imper',  'seidel'), rotation='+30')

ax.legend( (rects1[0], rects2[0], rects3[0]), ('gcc', 'graphite', 'polly') )

plt.show()
