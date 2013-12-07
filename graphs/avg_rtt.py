import numpy as np
import matplotlib.pyplot as plt


n_groups = 2

means_men = (2.13017239121, 1.47366317988)

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
plt.title('Average Round Trip Times')
plt.xticks(index+0.5, ('HTTP', 'HTTPS'))
plt.legend()

plt.show()
