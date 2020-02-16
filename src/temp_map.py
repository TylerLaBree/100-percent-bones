from astropy.table import Table
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt


def temp_vis(zoom_x, zoom_y, year, map_file='../processed_data/tmap.csv,'):
    # print('visualizing temperature')
    tmap = np.genfromtxt(map_file, delimiter=',')
    sb.set(font_scale=1)
    x_list = np.linspace(-20, 10, 30*zoom_x).astype(int)
    y_list = np.linspace(70, 50, 20*zoom_y).astype(int)
    x_ticks = np.linspace(0, len(x_list) - 1, 4,  dtype=np.int)
    y_ticks = np.linspace(0, len(y_list) - 1, 3,  dtype=np.int)
    x_tick_labels = [x_list[idx] for idx in x_ticks]
    y_tick_labels = [y_list[idy] for idy in y_ticks]

    ax = plt.axes()
    heat_map = sb.heatmap(tmap, xticklabels=x_tick_labels, yticklabels=y_tick_labels, cmap='coolwarm', zorder=2)
    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    ax.set_title('Temperature (°C) in {}'.format(year))
    plt.xlabel('Longitude (°E)')
    plt.ylabel('Latitude (°N)')
    return heat_map


def temp_arr(zoom_x, zoom_y, map_file='../processed_data/tmap.csv', data_file='../processed_data/clean_data.csv'):
    print('building temperature array')
    data = Table.read(data_file)
    data_table = data

    num_lat = 20
    num_long = 30

    npts = [[0 for x in range(num_long*zoom_x)] for y in range(num_lat*zoom_y)]
    tmap = [[0 for x in range(num_long*zoom_x)] for y in range(num_lat*zoom_y)]

    for d_pt in data_table:
        i = zoom_y*70 - int(np.math.floor(d_pt['lat']*zoom_y))-1
        j = int(np.math.floor(d_pt['long']*zoom_x)) + 20*zoom_x
        npts[i][j] += 1
        tmap[i][j] += d_pt['temp']

    for i in range(0, num_lat*zoom_y):
        for j in range(0, num_long*zoom_x):
            if npts[i][j] != 0:
                tmap[i][j] /= npts[i][j]
                npts[i][j] = np.math.floor(npts[i][j])
    np.savetxt(map_file, tmap, delimiter=',')
    return tmap


def change_temp(temp_change, in_file='../processed_data/tmap.csv', out_file='../processed_data/future_tmap.csv'):
    print('changing temperature by: ',temp_change)
    tmap1 = np.genfromtxt(in_file, delimiter=',')
    tmap2 = [[0 for x in range(len(tmap1[0]))] for y in range(len(tmap1))]

    for i in range(len(tmap1)):
        for j in range(len(tmap1[0])):
            tmap2[i][j] = tmap1[i][j] + temp_change
    np.savetxt(out_file, tmap2, delimiter=',')


def temp_from_year(year):
    temp = (year-2020)*0.035
    print('temperature change ', temp, ' C corresponds to year ', year)
    return temp


def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))


def fish_vis(mean, std, zoom_x, zoom_y, fish_type, year, map_file='../processed_data/tmap.csv'):
    num_lat = 20
    num_long = 30

    tmap = np.genfromtxt(map_file, delimiter=',')
    fmap = [[0 for x in range(num_long * zoom_x)] for y in range(num_lat * zoom_y)]

    for i in range(len(tmap)):
        for j in range(len(tmap[0])):
            fmap[i][j] = gaussian(tmap[i][j], mean, std)

    sb.set(font_scale=1)
    binsx = np.linspace(-20, 9, 30*zoom_x)
    binsx = binsx.astype(int)
    binsy = np.linspace(69, 50, 20*zoom_y)
    binsy = binsy.astype(int)
    ax = plt.axes()
    heat_map = sb.heatmap(fmap, xticklabels=binsx, yticklabels=binsy, cmap='OrRd',zorder=1)
    ax.set_title('Number of {} in {}'.format(fish_type,year))
    plt.xlabel('Longitude (°E)')
    plt.ylabel('Latitude (°N)')
    return heat_map
