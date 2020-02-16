from matplotlib.pyplot import show
import temp_map as t
import fishydata as f


mack_temp = (f.get_fish_temp(0) + f.get_fish_temp(1))/2
herr_temp = f.get_fish_temp(2)

heat_map = t.temp_vis(5, 10, map_file='../processed_data/future_tmap.csv')
fish_map = t.fish_vis(mack_temp, 0.3, 1, 2, map_file='../processed_data/future_tmap.csv')
show()



