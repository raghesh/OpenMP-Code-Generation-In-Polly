#/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 8
ind = np.arange(N)  # the x locations for the groups
width = 0.15       # the width of the bars
fig = plt.figure()
ax = fig.add_subplot(111)

gcc = (3.172690, 0.833520, 0.379887, 0.370590, 1.541867, 1.459991, 0.220855, 0.762357)
rects1 = ax.bar(ind, gcc, width, color='red') 

graphite = (2.908433, 0.613616, 0.378673, 0.378871, 1.323452, 1.449005, 0.100022, 0.618664)
rects2 = ax.bar(ind+width, graphite, width, color='black')

polly = (0.331969, 1.809630, 0.038285, 0.039890, 0.097274, 0.081309, 0.134631, 0.678914)
rects3 = ax.bar(ind+2*width, polly, width, color='blue')

# add some
ax.set_ylabel('Runtime')
ax.set_title('Polybench results(10 Core 64bit)')
ax.set_xticks(ind+width/2.0)
ax.set_xticklabels( ('2mm', 'adi', 'correlation', 'covariance', 'doitgen', 
		     'gemm', 'jacobi-2d-imper',  'seidel'), rotation='+30')

ax.legend( (rects1[0], rects2[0], rects3[0]), ('gcc', 'graphite', 'polly with openmp') )

plt.show()
