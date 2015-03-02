import matplotlib.pyplot as plt
import numpy as np

x = np.char.array(['Case_1','Case_2','Case_3'])
y = np.array([0,585074,16756])
colors = [
'lightskyblue',
'yellowgreen',
'lightcoral'
]
porcent = 100.*y/y.sum()

patches, texts = plt.pie(y, colors=colors, startangle=90)
labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(x, porcent)]


plt.legend(patches, labels, loc='upper center', bbox_to_anchor=(-0.1, 1.),
           fontsize=12)

plt.axis('equal')
plt.savefig('figure_6.png', bbox_inches='tight')
# plt.show()

