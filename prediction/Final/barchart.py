import datetime as dt
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
import numpy as np

labels = ['2020/02/09', '2020/02/10', '2020/02/11', '2020/02/12',
        '2020/02/13', '2020/02/14', '2020/02/15', '2020/02/16',
        '2020/02/17', '2020/02/18']

ongbm1 = [3809, 3971, 4140, 4315, 4496, 4683, 4876, 5076, 5284, 5497]
rongbm1 = [2918, 3677, 3411, 3715, 3869, 4448, 4548, 4960, 5237, 5610]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, ongbm1, width, label='ONGBM(1, 1)')
rects2 = ax.bar(x + width/2, rongbm1, width, label='RONGBM(1, 1)')

ax.set_ylabel('Daily infected cases', fontsize=18)
ax.set_xlabel('Date', fontsize=18)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()