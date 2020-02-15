from astropy.table import Table
import numpy as np

file = '../data/clean_data.csv'
data = Table.read(file)
data_table = data[0:5]

num_lat = 1
num_long = 1

npts = [[0 for x in range(num_lat)] for y in range(num_long)]
map = [[0 for x in range(num_lat)] for y in range(num_long)]

for i in range(0,num_lat):
    for j in range(0,num_long):
        min_lat = i+50
        min_long = j-2

        for d_pt in data_table:
            if (d_pt['lat'] > min_lat and d_pt['lat'] < min_lat+1 and d_pt['long'] > min_long and d_pt['long'] < min_long+1):
                npts[i][j]+= 1
                map[i][j] += d_pt['temp']

for i in range(0,num_lat):
    for j in range(0,num_long):
        map[i][j] /= npts[i][j]


print(npts)
print(map)