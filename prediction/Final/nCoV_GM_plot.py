import datetime as dt
from matplotlib import pyplot as plt
from matplotlib import dates as mdates

dates = ['01/28/2020','01/29/2020','01/30/2020','01/31/2020',
        '02/01/2020','02/02/2020','02/03/2020','02/04/2020',
        '02/05/2020','02/06/2020','02/07/2020','02/08/2020']

x = [dt.datetime.strptime(d, '%m/%d/%Y').date() for d in dates]
y = [[6061, 6061, 6061, 6061], [7816, 9946, 7258, 7130], [9821, 11451, 9822, 9824], [11948, 13185, 12418, 12378],
    [14551, 15181, 15098, 15056], [17387, 17479, 17898, 17860], [20626, 20125, 20842, 20793], [24553, 23172, 23953, 23862],
    [28276, 26679, 27251, 27068], [31439, 30719, 30755, 30417], [34875, 35369, 34483, 33915], [37552, 40724, 38455, 37564]]
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(x, y)
plt.legend(['Actual data', 'GM(1, 1)', 'NGBM(1, 1)', 'ONGBM(1, 1)'])
plt.gcf().autofmt_xdate()
plt.xlabel("Date", fontsize = 18)
plt.ylabel("Total infected cases", fontsize = 18)
plt.show()