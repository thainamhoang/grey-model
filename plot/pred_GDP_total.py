import numpy as np
import pandas as pd
# import datetime as dt
from matplotlib import pyplot as plt
# from matplotlib import dates as mdates

data = pd.read_csv('/Users/thainam/Documents/GitHub/grey-model/data/plot/pred_GDP_total.csv')

year = data.iloc[:, :1].to_numpy() #Type :pd.DataFrame to numpy.ndarray
year = np.reshape(year, len(year))
year = year.tolist()
# year = list(map(str, year))

# x = [dt.datetime.strptime(d, '%Y').date() for d in year]
y = data.iloc[:, 1:6].to_numpy().tolist()

plt.plot(year, y, marker='o')
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# plt.gca().xaxis.set_major_locator(mdates.YearLocator())
# plt.gcf().autofmt_xdate()
plt.xlabel("Year", fontsize=20)
plt.ylabel("GDP (billion US$)", fontsize=20)
plt.legend(['Actual data', 'GBM(1, 1)', 'NGBM(1, 1)', 'ONGBM(1, 1)', 'RONGBM(1, 1)'])
plt.tick_params(axis='both', which='major', labelsize=12)
plt.show()