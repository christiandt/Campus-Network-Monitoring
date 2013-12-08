"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt


n_groups = 3


usage = (64653855, 36008406, 37311035)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.5

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, usage, bar_width,
                 alpha=opacity,
                 color='black',
                 error_kw=error_config,
                 label='')

plt.xlabel('')
plt.ylabel('Packets')
plt.title('Total Distribution of Packets')
plt.xticks(index + (bar_width/2), ('Total', 'Filter 1', 'Filter 2'))
plt.legend()

plt.tight_layout()
plt.show()
