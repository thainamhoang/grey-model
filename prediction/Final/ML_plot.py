import datetime as dt
from matplotlib import pyplot as plt
from matplotlib import dates as mdates

dates = ['01/28/2020','01/29/2020','01/30/2020','01/31/2020',
        '02/01/2020','02/02/2020','02/03/2020','02/04/2020',
        '02/05/2020','02/06/2020','02/07/2020','02/08/2020',]

x = [dt.datetime.strptime(d, '%m/%d/%Y').date() for d in dates]
y = [[6061, 6061, 6061], [7816, 8836, 8707], [9821, 10184, 10213], [11948, 12395, 12486],
    [14551, 14481, 14621], [17387, 17371, 17464], [20626, 21294, 21269], [24553, 23061, 22928],
    [28276, 27808, 27837], [31439, 31649, 31717], [34875, 34727, 34757], [37552, 38285, 38197]]
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(x, y)
plt.legend(['Actual data', 'ANN', 'LSTM'])
plt.gcf().autofmt_xdate()
plt.xlabel("Date", fontsize = 18)
plt.ylabel("Total infected cases", fontsize = 18)
plt.show()