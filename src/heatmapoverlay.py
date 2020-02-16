import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.pyplot import show
import seaborn as sb
import numpy as np
import temp_map as t

zoom_x=1
zoom_y=2
map_file='../processed_data/tmap.csv'
num_file='..processed_data/'
tmap = np.genfromtxt(map_file, delimiter=',')
sb.set(font_scale=1)
binsx = np.linspace(-20, 9, 30 * zoom_x)
binsx = binsx.astype(int)
binsy = np.linspace(69, 50, 20 * zoom_y)
binsy = binsy.astype(int)


fish_map = t.fish_vis()
heat_map = sb.heatmap(tmap, xticklabels=binsx, yticklabels=binsy, cmap='coolwarm',alpha=0.75,zorder=2)

