import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.pyplot import show
import seaborn as sb
import numpy as np

zoom_x=1
zoom_y=2
map_file='../processed_data/tmap.csv'
tmap = np.genfromtxt(map_file, delimiter=',')
sb.set(font_scale=1)
binsx = np.linspace(-20, 9, 30 * zoom_x)
binsx = binsx.astype(int)
binsy = np.linspace(69, 50, 20 * zoom_y)
binsy = binsy.astype(int)

heat_map = sb.heatmap(tmap, xticklabels=binsx, yticklabels=binsy, cmap='coolwarm',alpha=0.5,zorder=2)
img = mpimg.imread('../img/UK.png')
heat_map.imshow(img,aspect=heat_map.get_aspect(),extent=heat_map.get_xlim()+heat_map.get_ylim(),zorder=1)
show()
