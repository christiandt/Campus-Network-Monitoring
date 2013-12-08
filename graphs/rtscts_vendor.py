"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt


n_groups = 10


usage = (75.75, 9.51, 6.49, 4.29, 1.78, 1.17, 0.47, 0.32, 0.22, 0.08)

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

plt.xlabel('Hardware Vendor')
plt.ylabel('Percent')
plt.title('RTS/CTS Hardware Vendor')
plt.xticks(index + (bar_width/2), ('Cisco', 'HonHai', 'LiteOn', 'Apple', 'Azurewave', 'Chicony', 'Samsung', 'Intel', 'LG', 'Other'))
#plt.ylim([0,100])
plt.legend()

plt.tight_layout()
plt.show()
