import numpy as np
import matplotlib.pyplot as plt


n_groups = 2

means_men = (10.3195666292, 36.8868973238)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.9

opacity = 0.5
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, means_men, bar_width,
                 alpha=opacity,
                 color='black',
                 error_kw=error_config)

#plt.xlabel('Group')
plt.ylabel('Time')
plt.title('Avg Session Length')
plt.xticks(index+(bar_width/2), ('HTTP', 'HTTPS'))
plt.legend()

plt.show()
