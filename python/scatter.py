import numpy as np, matplotlib.pyplot as plt,random

a=random.randint(0,19920613)
np.random.seed(a)
x=np.arange(0.0,100.0,5.0)
y=(x*1.5)+np.random.rand(20)*50

plt.scatter(x,y,c='b',alpha=0.5, label='scatter point')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.title('scatter plot')
plt.show()
