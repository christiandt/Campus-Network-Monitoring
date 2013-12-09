"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt


n_groups = 2


usage = (64653855, 20533866)

fig, ax = plt.subplots()
fig.set_size_inches(4.5,6.0)

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
plt.title('Goodput vs Throughput')
plt.xticks(index + (bar_width/2), ('Throughput', 'Goodput'))
plt.legend()

plt.tight_layout()
plt.show()
