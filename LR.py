import numpy as np
import matplotlib.pyplot as plt
import math

def gradiant_desc(mat_X,Y):
    '''
    mat_X 为n*m，xi为m维行向量
    Y为n维列向量
    '''
    theta = np.zeros((mat_X.shape[1]+1,1))
    oness = np.ones((mat_X.shape[0],1))
    mat_X = np.hstack((oness,mat_X))
    times = 5000
    step = 0.001
    strain = 0.01
    #while 1:
    for j in range(times) :
        for i in range(mat_X.shape[1]):
            #print(type(np.matmul(mat_X , theta) )

            h = sigmod(np.matmul(mat_X , theta) )
            err = h - Y
            theta[i] = theta[i] - step*np.matmul(mat_X[:,i].transpose() , err)
            #print(theta)
        if theta.sum()/theta.size < strain :
            break
    return theta

def sigmod(x):
    return 1.0/(1+np.exp(-x))

# wrong : file_dir = "C:\Users\sunRIZ_\octavefiles\pimapima-indians-diabetes.csv"
#file_dir = r"pima-indians-diabetes.csv"
#f = csv.reader(open(file_dir))
#dataX = [[1,3],[2,4],[5,6],[9,3],[5,1],[-1,-5],[-9,-2],[-6,-7],[-1,-2]]
#dataY = [[1],[1],[1],[1],[1],[0],[0],[0],[0]]

x =           [[1, 0, 0, 0, 0, 0, .697, .46],
              [0, 0, 1, 0, 0, 0, .774, .376],
              [0, 0, 0, 0, 0, 0, .634, .264],
              [1, 0, 1, 0, 0, 0, .608, .318],
              [2, 0, 0, 0, 0, 0, .556, .215],
              [1, 1, 0, 0, 1, 1, .403, .237],
              [0, 1, 0, 1, 1, 1, .481, .149],
              [0, 1, 0, 0, 1, 0, .437, .211],
              [0, 1, 1, 1, 1, 0, .666, .091],
              [1, 2, 2, 0, 2, 1, .243, .267],
              [2, 2, 2, 2, 2, 0, .245, .057],
              [2, 0, 0, 2, 2, 1, .343, .099],
              [1, 1, 0, 1, 0, 0, .639, .161],
              [2, 1, 1, 1, 0, 0, .657, .198],
              [0, 1, 0, 0, 1, 1, .36, .37],
              [2, 0, 0, 2, 2, 0, .593, .042],
              [1, 0, 1, 1, 1, 0, .719, .103]]

y = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0]

print(x[:10,6])

dataX = list(x[:10,6:])
dataY = y

px1 = []
px2 = []
for x in dataX:
    px1.append(x[0])
    px2.append(x[1])
plt.scatter(px1,px2,75,px1)
plt.xlim(0,1)
plt.ylim(0,1)

'''
for row in f:
    dataX.append(row[:-1])
    dataY.append([row[-1]])
'''

mat_X = np.array(dataX,dtype=float)
mat_Y = np.array(dataY,dtype=float)
#print(mat_X)
#print(mat_Y)
theta = gradiant_desc(mat_X,mat_Y)
xx = np.linspace(-10,10,256,endpoint=True)
yy = -(theta[1]/theta[2]*x + theta[0])
plt.plot(xx,yy)

'''
prediction = sigmod(np.matmul(np.hstack((np.ones((mat_X.shape[0],1)),mat_X)),theta))
err = prediction - mat_Y
print(err)
print(abs(err).sum())
print(theta)
'''

plt.show()
#print(theta)
