import numpy as np
import matplotlib.pyplot as plt


n_groups = 25

means_men = (105, 35, 25, 15, 15, 13, 11, 9, 9, 9, 9, 8, 7, 7, 6, 5, 4, 3, 3, 2, 2, 2, 2, 2, 2)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.9

opacity = 0.5
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, means_men, bar_width,
                 alpha=opacity,
                 color='black',
                 error_kw=error_config)

plt.xlabel('Applications')
plt.ylabel('Unique MACs')
plt.title('Applications used on more than one device')
plt.xticks(index+0.5, ('dropbox', 'itunes', 'instagram', 'facebook', 'skype', 'mail', 'appstore', 'snapchat', 'twc', 'sogou', 'spotify', 'shockwave', 'pandora', 'anyconnect', 'avast', 'youtube', 'devicescape', 'yodao', 'adobe', 'yelp', 'rainmeter', 'kakaotalk', 'octoshape', 'unity', 'seaport'), rotation='vertical')
plt.legend()

plt.show()
