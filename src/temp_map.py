from astropy.table import Table
import numpy as np

file = '../data/clean_data.csv'
data = Table.read(file)
data_table = data

num_lat = 20
num_long = 30

npts = [[0 for x in range(num_long)] for y in range(num_lat)]
map = [[0 for x in range(num_long)] for y in range(num_lat)]

for i in range(0, num_lat):
    for j in range(0, num_long):
        min_lat = i+50
        min_long = j-20

        for d_pt in data_table:
            if min_lat < d_pt['lat'] < min_lat+1 and min_long < d_pt['long'] < min_long+1:
                npts[i][j] += 1
                map[i][j] += d_pt['temp']

for i in range(0, num_lat):
    for j in range(0, num_long):
        if npts[i][j] != 0:
            map[i][j] /= npts[i][j]
            npts[i][j] = np.math.floor(npts[i][j])

print(npts)
print(map)

np.savetxt('../data/npts.csv', npts, delimiter=',')
np.savetxt('../data/tmap.csv', map, delimiter=',')
