import numpy as np

#半小时结果：3.13267216
n = 20000
randx = np.random.randint(0,1000,n)/500
randy = randx
nx = 0
for x in randx:
    for y in randy:
        if (x-1)**2+(y-1)**2 < 1 :
            nx += 1
pi = nx/(n**2)*4
print(pi)
