"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt


n_groups = 2


usage = (24338189029, 16348461868)

fig, ax = plt.subplots()
fig.set_size_inches(4.0,6.0)

index = np.arange(n_groups)
bar_width = 0.5

opacity = 0.5
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, usage, bar_width,
                 alpha=opacity,
                 color='black',
                 error_kw=error_config)

plt.xlabel('')
plt.ylabel('Bytes')
plt.title('Goodput vs Throughput')
plt.xticks(index + (bar_width/2), ('Throughput', 'Goodput'))
plt.legend()

plt.tight_layout()
plt.show()
