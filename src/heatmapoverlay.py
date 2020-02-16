import matplotlib.pyplot as plt
import temp_map as t
import reduce_data as r

def overlay_vis(year, fish_type, fish_temp, zoom_x, zoom_y):

    #r.clean(1900)
    #t.temp_arr(zoom_x, zoom_y, map_file='../processed_data/tmap.csv')
    t.change_temp(year, zoom_x, zoom_y)


    ax = plt.axes()
    heat_map = t.temp_vis(zoom_x, zoom_y, year, map_file='../processed_data/future_tmap.csv', alpha=0.5)
    fish_map = t.fish_vis(fish_temp, 0.3,zoom_x, zoom_y, fish_type, year, map_file='../processed_data/future_tmap.csv', cmap='Greys')
    ax.set_title('{} Location/Temperature in {}'.format(fish_type, year))
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.show()



