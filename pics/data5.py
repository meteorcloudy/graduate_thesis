import matplotlib.pyplot as plt
import numpy as np

x = np.char.array(['Case_1_1','Case_1_2','Case_1_3','Case_1_4_1','Case_1_4_2','Case_1_4_3','Case_2_1','Case_2_2','Case_2_3','Case_2_4'])
y = np.array([0,251962,0,5101,0,0,0,13662,0,0])
colors = [
'lightskyblue',
'yellowgreen',
'white',
'gold',
'grey',
'pink',
'darkgreen',
'lightcoral',
'blue',
'yellow',
'red',
'violet'
]
porcent = 100.*y/y.sum()

patches, texts = plt.pie(y, colors=colors, startangle=90)
labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(x, porcent)]


plt.legend(patches, labels, loc='upper center', bbox_to_anchor=(-0.1, 1.),
           fontsize=12)

plt.axis('equal')
plt.savefig('figure_5.png', bbox_inches='tight')
# plt.show()

