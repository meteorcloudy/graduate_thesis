import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7,8,9,12,17]
y1 = [0.0015,0.00225,0.00271429,0.00388889,0.0062,0.0065,0.023,0.0265,0.022,0.534,21.034]
y2 = [0.00158333,0.002,0.00271429,0.00311111,0.0044,0.0055,0.01025,0.0205,0.013,0.1735,3.916]


line1, = plt.plot(x, y1, 'bd-', label = 'FPT')
line2, = plt.plot(x, y2, 'ro-', label = 'FPT_faster')


plt.legend(loc=4)


plt.ylabel('Time(s)')
plt.xlabel('rSPR distance')
# plt.title('the comparison between previous and imporved algorithm')

plt.show()