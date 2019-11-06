import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,100,100)
y = 15*x+5+np.random.normal(0,40,len(x))
X = np.mean(x)
Y = np.mean(y)

nr = 0
dr = 0
XY = 0
xs=0
ys=0

for _x,_y in zip(x,y):
    nr += (_x-X)*(_y-Y)
    dr += (_x-X)**2
    XY+=_x*_y
    xs+=_x**2
    ys+=_y**2
beta1 = nr/dr
beta0 = Y-beta1*X

y2 = beta0+beta1*x

plt.scatter(x,y,color='green')
plt.plot(x,y2)

nr = 0
dr = 0
n = len(x)
rho = n*(XY-X*n)*(Y*n)/((n*xs-(X*n)**2)*(n*ys-(n*Y)**2))**0.5

SSR=0
SST=0
for _y,_y2 in zip(y,y2):
    SSR+= (_y2-_y)**2
    SST+=(_y-Y)**2

Rs = 1-(SSR/SST)

print("R square",Rs)
plt.show()
