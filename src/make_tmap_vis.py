import temp_map as t
import reduce_data as r

print('cleaning data')
r.clean(1960)
print('building temp array')
t.temp_arr(4, 8)
print('visualizing temperature')
t.temp_vis(4, 8)
