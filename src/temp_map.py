from astropy.table import Table
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt


def temp_vis(zoom_x, zoom_y):
    tmap = np.genfromtxt("../processed_data/tmap.csv", delimiter=',')
    sb.set(font_scale=1)
    binsx = np.linspace(-20, 9, 30*zoom_x)
    binsx = binsx.astype(int)
    binsy = np.linspace(69, 50, 20*zoom_y)
    binsy = binsy.astype(int)
    heat_map = sb.heatmap(tmap, xticklabels=binsx, yticklabels=binsy, cmap='coolwarm')
    plt.show()


def temp_arr(zoom_x, zoom_y):
    file = '../processed_data/clean_data.csv'
    data = Table.read(file)
    data_table = data

    num_lat = 20
    num_long = 30

    npts = [[0 for x in range(num_long*zoom_x)] for y in range(num_lat*zoom_y)]
    tmap = [[0 for x in range(num_long*zoom_x)] for y in range(num_lat*zoom_y)]

    for d_pt in data_table:
        i = zoom_y*50 - int(np.math.floor(d_pt['lat']*zoom_y))
        j = int(np.math.floor(d_pt['long']*zoom_x)) + 20*zoom_x
        npts[i][j] += 1
        tmap[i][j] += d_pt['temp']

    for i in range(0, num_lat*zoom_y):
        for j in range(0, num_long*zoom_x):
            if npts[i][j] != 0:
                tmap[i][j] /= npts[i][j]
                npts[i][j] = np.math.floor(npts[i][j])

    np.savetxt('../processed_data/npts.csv', npts, delimiter=',')
    np.savetxt('../processed_data/tmap.csv', tmap, delimiter=',')
