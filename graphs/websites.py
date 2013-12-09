import numpy as np
import matplotlib.pyplot as plt


n_groups = 20

means_men = (4.770, 4.002, 3.931, 2.710, 2.668, 2.503, 2.229, 2.015, 1.964, 1.892, 1.621, 1.660, 1.600, 1.581, 1.365, 1.342, 1.093, 0.975, 0.925, 0.845)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.9

opacity = 0.5
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, means_men, bar_width,
                 alpha=opacity,
                 color='red',
                 error_kw=error_config,
                 hatch="//")

plt.xlabel('')
plt.ylabel('Requests in %')
plt.title('20 Most Requested URLs')
plt.xticks(index+0.5, ('*.akamaitechnologies.com', '*.1e100.net', '*.apple.com', '*.youtube.com', '*.ucsb.edu', '*.ucsb.edu', '*.google.com', '*.doubleclick.net', '*.yimg.com', '*.ytimg.com', '*.google-analytics.com', '*.facebook.com', '*.scorecardresearch.com', '*.instagram.com', '*.dropbox.com', '*.wikimedia.org', '*.baidu.com', '*.nflximg.net', '*.yahoo.com', '*.fbcdn.net'), rotation='vertical')
plt.legend()

plt.tight_layout()

plt.show()
