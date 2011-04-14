#/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 8
ind = np.arange(N)  # the x locations for the groups
width = 0.15       # the width of the bars
fig = plt.figure()
ax = fig.add_subplot(111)

gcc = (1.976261, 0.418657, 0.338003, 0.336355, 0.560561, 0.809508, 0.234721, 0.310160)
rects1 = ax.bar(ind, gcc, width, color='red') 

graphite = (1.622490, 0.461362, 0.338462, 0.334376, 0.490987, 0.859278, 0.218231, 0.309659)
rects2 = ax.bar(ind+width, graphite, width, color='black')

polly = (1.031165, 0.462340, 0.198239, 0.199907, 0.340958, 0.346735, 0.225501, 0.459641)
rects3 = ax.bar(ind+2*width, polly, width, color='blue')

# add some
ax.set_ylabel('Runtime')
ax.set_title('Polybench results(2 Core 64bit)')
ax.set_xticks(ind+width/2.0)
ax.set_xticklabels( ('2mm', 'adi', 'correlation', 'covariance', 'doitgen', 
		     'gemm', 'jacobi-2d-imper',  'seidel'), rotation='+30')

ax.legend( (rects1[0], rects2[0], rects3[0]), ('gcc', 'graphite', 'polly') )

plt.show()
