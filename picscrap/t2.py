import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10,0.1)
y1 = np.sin(x)
y2 = np.cos(x)

#fig,(ax) = plt.subplots()
plt.plot(x,y1,'r--')
plt.plot(x,y2)
#plt.savefig("pic")
plt.tight_layout()
plt.show()
