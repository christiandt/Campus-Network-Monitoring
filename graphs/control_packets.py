"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt


n_groups = 2


usage = (28645449, 36008406)

fig, ax = plt.subplots()
fig.set_size_inches(4.0,6.0)

index = np.arange(n_groups)
bar_width = 0.5

opacity = 0.5
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, usage, bar_width,
                 alpha=opacity,
                 color='black',
                 error_kw=error_config,
                 label='')

plt.xlabel('')
plt.ylabel('Packets')
plt.title('Total Distribution of Packets')
plt.xticks(index + (bar_width/2), ('Data', 'Control Packets'))
plt.legend()

plt.tight_layout()
plt.show()
