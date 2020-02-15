from astropy.table import Table
import numpy as np
#lat, long, weight
mack_ns=[[60,-1,4],[60.5,-1,3],[59.5,-1,3],[59,-1,2],[59.5,0,2],[60,0,1],[59.5,1,1],[60,1,2],[60.5,-2,4],[60,-2,5],[59.5,-2,4],[59,-2,3],[58.5,-2,2],[60,-3,5],[59.5,-3,3]]
mack_na=[[59.5,-6,1],[59,-6,2],[59.5,-7,2],[59,-7,5],[59,-8,1],[58.5,-8,5],[58.5,-9,1],[57,-9,3],[57,-10,2],[57.5,-10,3],[57,-10,2],[56.5,-10,2],[56.5,-9,2],[56,-10,1],[55.5,-10,2],[55,-10,4],[54.5,-11,2],[54,-11,2],[53.5,-12,3],[53,-12,2],[52.5,-12,2],[52,-12,3],[51.5,-12,2]]
herr_ns=[[57,-2,3],[57,-1,4],[57.5,0,2],[57.5,1,1],[58,-1,2],[58,0,5],[58,1,2],[58.5,-1,4],[58.5,0,5],[58.5,1,1],[59,0,3],[59,-1,3],[59,-2,2],[59,-3,1],[59.5,-3,3],[59,-4,1],[59,-5,2],[58.5,-5,1],[59.5,-4,2],[59.5,-3,1],[59.5,-2,1],[59.5,-1,1]]

data=Table.read('../processed_data/clean_data.csv')
#print(data)

file=open('fishytemps.csv','a+')
singletemp=[]
temparray=[]
weightarray=[]
count=0
for i in range(len(herr_ns)):
    lat = herr_ns[i][0]
    long = herr_ns[i][1]
    for elt in data:
        if lat < elt['lat'] < lat+0.5 and long < elt['long'] < long+1:
            singletemp.append(elt['temp'])
            count+=1
    x=np.sum(singletemp)
    y=x/count
    temparray.append(y*herr_ns[i][2])
    weightarray.append(herr_ns[i][2])
    #print(singletemp)

totalweight= np.sum(weightarray)
totaltemp = np.sum(temparray)
average = str(totaltemp/totalweight)
file.write(average)
print("North Sea Herring: ", totaltemp/totalweight)



