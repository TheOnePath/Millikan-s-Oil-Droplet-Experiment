""" Millikan's Oil Droplet Experiment """

import csv
import numpy as np
import matplotlib.pyplot as plt
import math

# Constants
charge_ofElectron = 1.6021765e-19
a = 7.776e-8
pi = math.pi
g = 9.81
p = dens_ofOil = 877
pAir = dens_ofAir = 1.16
rho = 2*((p - pAir)*g)
plateDist = 0.006

# Lists
timeList = []
voltageList = []
distList = []

# Get file
file_nm = str(input("Enter the file name: ")+".csv")
data = np.genfromtxt(file_nm,delimiter=',')

# Axis variables
time = data[:,0]
voltage = data[:,1]
dist = data[:,2]
X = []
Y = []
xfit = None
yfit = None

# Variables
times = 0
tIndex = 0
VIndex = 0
dIndex = 0

def formulas():
    global times
    global tIndex
    global VIndex
    global dIndex
    while times <= 11:
        t = time[tIndex]
        V = voltage[VIndex]
        d = dist[dIndex]
        v = d/t
        n = Visc_ofAir = 1.789*10**-5
        r = ((9*n*v)/rho)**(1/2)
        qSqrt = (n**3*v**3/(2*(p - pAir)*g))**(1/2)
        q = 18*pi*plateDist/V*qSqrt
        X.append(r)
        Y.append(q)
        tIndex += 1
        VIndex += 1
        dIndex += 1
        times += 1
    sort()

def graph():
    global xfit
    global yfit
    xmin = x[0]
    xmax = x[len(x)-1]
    print(xmin,xmax)
    interval = (xmax-xmin)/99
    coefs = np.polyfit(x, y, 2)
    print(coefs)
    xfit = np.arange(xmin,xmax+interval,interval)
    yfit = np.polyval(coefs,xfit)

def sort():
    global X
    global Y
    global x
    global y
    ord1 = np.array(X)
    ord2 = np.array(Y)
    orig_array = np.column_stack([ord1,ord2])
    #order_array = np.array(1)
    data = sort_array = orig_array[orig_array[:,0].argsort()]
    x = data[:,0]
    y = data[:,1]
    graph()

for i in range(len(X),0):
    t = data[tIndex,0]
    V = data[VIndex,1]
    dist = data[dIndex,2]
    timeList.append(t)
    voltageList.append(V)
    distList.append(dist)
    print(timeList,voltageList,distList)

tIndex = 0
VIndex = 0
dIndex = 0
formulas()

# Plot and Show graph
plt.plot(x,y,'ro',xfit,yfit)
##plt.plot(x,y,'ro')
plt.show()
