import matplotlib.pyplot as plt
import temp_map as t
import fishydata as f
import reduce_data as r

year=2070
#r.clean(1900)
#t.temp_arr(zoom_x, zoom_y, map_file='../processed_data/tmap.csv')
#t.change_temp(t.temp_from_year(2070))

zoom_x=2
zoom_y=4

mack_temp = (f.get_fish_temp(0) + f.get_fish_temp(1))/2
herr_temp = f.get_fish_temp(2)

fish='Mackerel'
#fish='Herring'
fish_temp=mack_temp
#fish_temp=herr_temp

ax = plt.axes()
heat_map = t.temp_vis(zoom_x, zoom_y, year, map_file='../processed_data/future_tmap.csv', alpha=0.5)
fish_map = t.fish_vis(fish_temp, 0.3,zoom_x, zoom_y, fish, year, map_file='../processed_data/future_tmap.csv', cmap='Greys')
ax.set_title('{} Location/Temperature in {}'.format(fish, year))
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()



