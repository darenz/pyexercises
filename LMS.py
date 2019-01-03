import numpy as np
import matplotlib.pyplot as plt

#data = [(1,3,9),(3,9,15),(4,7,30),(6,11,57),(8,20,90),(10,45,120)]
data = [(1,3),(3,9),(4,7),(6,11),(8,20),(10,45)]
x0 = []
y0 = []
for i in range(len(data)) :
    x0.append(data[i][0])
    y0.append(data[i][1])

x = np.asarray(x0)
y = np.asarray(y0)

xTx = np.matmul(x.T,x)
nomaltheta = np.matmul(np.matmul(xTx.I,x.T),y)

plt.scatter(x,y)

alpha = 0.001
theta = np.zeros(len(data[0]))

err = 0.1
em = 100 

while em>err:
    for j in range(len(theta)) :
        s = 0
        for i in range(len(x)):
            xi = np.array([1])
            xi = np.append(xi,x[i])
            hxi = np.matmul(theta,xi)
            s += (hxi - y[i])*xi[j]
        e = alpha*s
        em = abs(e)
        theta[j] = theta[j] - e

print(theta)
print(nomaltheta)

X = np.linspace(-2,15,256,endpoint=True)
#Y = np.linspace(0,50,256,endpoint=True)
#Hx = theta[0]+theta[1]*X+theta[2]*Y
Hx = theta[0]+theta[1]*X
plt.plot(X,Hx)
plt.show()

