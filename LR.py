import numpy as np
import matplotlib.pyplot as plt

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
dataX = [[1,3],[2,4],[5,6],[9,3],[5,1],[-1,-5],[-9,-2],[-6,-7],[-1,-2]]
dataY = [[1],[1],[1],[1],[1],[0],[0],[0],[0]]
plt.scatter(dataX,dataY)
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
x = np.linspace(-10,10,256,endpoint=True)
plt.plot(x,theta[0] + theta[1]*x)

prediction = sigmod(np.matmul(np.hstack((np.ones((mat_X.shape[0],1)),mat_X)),theta))
err = prediction - mat_Y
print(err)
print(abs(err).sum())
print(theta)
plt.show()
#print(theta)