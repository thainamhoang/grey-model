from matplotlib import pyplot as PLT

fig = PLT.figure()

ax1 = fig.add_subplot(211)
ax1.plot([(1, 2), (3, 4)], [(4, 3), (2, 3)])

ax2 = fig.add_subplot(212)
ax2.plot([(7, 2), (5, 3)], [(1, 6), (9, 5)])

PLT.show()