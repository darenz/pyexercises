import numpy as np

def gradiant_desc(mat_X,Y):
    '''
    mat_X 为n*m，xi为m维行向量
    Y为n维列向量
    '''
    theta = np.zeros((n,1))
    for i in range(Y):
        h = sigmod(mat_X * theta)
        err = h - Y
        theta[i] = mat_X[i] * err
    return theta

def sigmod(x):
    return 1.0/(1+np.exp(-x))


