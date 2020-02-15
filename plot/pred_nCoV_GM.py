import numpy as np
import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt
from matplotlib import dates as mdates

data = pd.read_csv('/Users/thainam/Documents/GitHub/grey-model/data/plot/pred_nCoV_GM.csv')

dates = data.iloc[:, :1].to_numpy() #Type :pd.DataFrame to numpy.ndarray
dates = np.reshape(dates, len(dates))
dates = dates.tolist()
x = [dt.datetime.strptime(d, '%m/%d/%Y').date() for d in dates]

y = data.iloc[:, 1:4].to_numpy()
y = y.tolist()

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(x, y, marker='o')
plt.legend(['Actual data', 'ONGBM(1, 1)', 'RONGBM(1, 1)'])
plt.gcf().autofmt_xdate()
plt.xlabel("Date", fontsize=20)
plt.ylabel("Total infected cases", fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.show()