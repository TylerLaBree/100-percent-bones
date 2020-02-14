from astropy.table import Table
import numpy as np

npts = []
map = []

num_lat = 20
num_long = 20

for i in range(0,num_lat):
    for j in range(0,num_long):
        min_lat = i-20
        min_long = j-20
        for d_pt in data:
            if (d_pt['lat'] > min_lat & d_pt['lat'] < min_lat+1 & d_pt['long'] > min_long & d_pt['long'] < min_long+1):
                npts[i,j]++
                map[i,j] += d_pt['temp']

print(npts)
print(map)