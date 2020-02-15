import temp_map as t
import reduce_data as r
import fishydata as f

zoom_x = 1
zoom_y = 2

# r.clean(2000)
t.temp_arr(zoom_x, zoom_y)
# t.temp_vis(zoom_x, zoom_y)

t.change_temp(t.temp_from_year(2270))
t.temp_vis(zoom_x, zoom_y, map_file='../processed_data/tmap.csv')


# t.temp_arr(1, 2, map_file='../processed_data/low_res_tmap.csv')
# mack_temp = (f.get_fish_temp(0) + f.get_fish_temp(1))/2
# herr_temp = f.get_fish_temp(2)
#
# print('mackerel plot at temp: ', mack_temp)
# t.fish_vis(mack_temp, 0.3, zoom_x, zoom_y)
# print('herring plot at temp: ', herr_temp)
# t.fish_vis(herr_temp, 0.3, zoom_x, zoom_y)
