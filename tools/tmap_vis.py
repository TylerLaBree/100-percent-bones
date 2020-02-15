import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

tmap = np.genfromtxt("../data/tmap.csv",delimiter=',')
sb.set(font_scale=1)
binsx=np.linspace(-20,9,30)
binsx=binsx.astype(int)
binsy=np.linspace(69,50,20)
binsy=binsy.astype(int)
heat_map = sb.heatmap(tmap, xticklabels=binsx, yticklabels=binsy, annot=True, cmap='coolwarm')
plt.show()