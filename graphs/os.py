"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt


n_groups = 10


old = (25.855, 51.020, 20.650, 0.00, 0.00, 0.380, 0.985, 0.577, 0.380, 0.155)

new = (42.111, 21.721, 14.652, 11.270, 9.631, 0.615, 0, 0, 0, 0)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, old, bar_width,
                 alpha=opacity,
                 color='black',
                 error_kw=error_config,
                 label='2004')

rects2 = plt.bar(index + bar_width, new, bar_width,
                 alpha=opacity,
                 color='red',
                 error_kw=error_config,
                 label='2013')

plt.xlabel('Operating System')
plt.ylabel('Percent')
plt.title('OS user share')
plt.xticks(index + bar_width, ('OSX', 'Windows', 'Unknown', 'Android', 'iOS', 'Linux', 'Vocera', 'Palm OS', 'Cisco\n VoIP', 'pocket PC'))
plt.legend()

plt.tight_layout()
plt.show()
