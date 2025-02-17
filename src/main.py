import temp_map as t
import reduce_data as r
import fishydata as f
import matplotlib.pyplot as plt

zoom_x = 2
zoom_y = 4
#
#clean data and create temperature array
#r.clean(1900, data_file='../processed_data/clean_data_1900.csv')
#r.clean(2010, data_file='../processed_data/clean_data_2010.csv')

#t.temp_arr(zoom_x, zoom_y)
#
# # find fish preferred temps
# t.temp_arr(1, 2, map_file='../processed_data/low_res_tmap.csv')
mack_temp = (f.get_fish_temp(0) + f.get_fish_temp(1))/2
herr_temp = f.get_fish_temp(2)
#
# # create future temperature array
# t.change_temp(t.temp_from_year(2070))

# visualize data:
t.temp_vis(zoom_x, zoom_y, map_file='../processed_data/tmap.csv',year=2020)
plt.show()
t.temp_vis(zoom_x, zoom_y, map_file='../processed_data/future_tmap.csv',year=2070)
plt.show()
print('current mackerel plot at temp: ', mack_temp)
t.fish_vis(mack_temp, 0.3, zoom_x, zoom_y, 'Mackerel', map_file='../processed_data/tmap.csv',year=2020)
plt.show()
print('future mackerel plot at temp: ', mack_temp)
t.fish_vis(mack_temp, 0.3, zoom_x, zoom_y, 'Mackerel', map_file='../processed_data/future_tmap.csv',year=2070)
plt.show()
print('current herring plot at temp: ', herr_temp)
t.fish_vis(herr_temp, 0.3, zoom_x, zoom_y, 'Herring',year=2020)
plt.show()
print('future herring plot at temp: ', herr_temp)
t.fish_vis(herr_temp, 0.3, zoom_x, zoom_y, 'Herring', map_file='../processed_data/future_tmap.csv', year=2070)
plt.show()
