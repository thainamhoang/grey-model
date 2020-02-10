import datetime as dt
from matplotlib import pyplot as plt
from matplotlib import dates as mdates

dates = ['01/28/2020','01/29/2020','01/30/2020','01/31/2020',
        '02/01/2020','02/02/2020','02/03/2020','02/04/2020',
        '02/05/2020','02/06/2020','02/07/2020','02/08/2020',
        '02/09/2020','02/10/2020','02/11/2020','02/12/2020',
        '02/13/2020','02/14/2020','02/15/2020','02/16/2020',
        '02/17/2020','02/18/2020']

x = [dt.datetime.strptime(d, '%m/%d/%Y').date() for d in dates]
y= [[6061, 6061, 6061], [7816, 7130, 7258], [9821, 9824, 9822], [11948, 12378, 12418],
    [14551, 15056, 15098], [17387, 17860, 17898], [20626, 20793, 20842], [24553, 23862, 23953],
    [28276, 27068, 27251], [31439, 30417, 30755], [34875, 33915, 34483], [37552, 37564, 38455],
    [None, 41373, 41373], [None, 45344, 45050], [None, 49484, 48461], [None, 53799, 52176],
    [None, 58295, 56045], [None, 62978, 60493], [None, 67854, 65041], [None, 72930, 70001],
    [None, 78214, 75238], [None, 83711, 80848]]
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(x, y)
plt.legend(['Actual data', 'ONGBM(1, 1)', 'RONGBM(1, 1)'])
plt.gcf().autofmt_xdate()
plt.xlabel("Date", fontsize = 18)
plt.ylabel("Total infected cases", fontsize = 18)
plt.show()