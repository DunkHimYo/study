import matplotlib.pyplot as plt
import numpy as np
import math
import time

np.random.seed(100)
X= 0

N=1000

circle_x=np.arange(0,1,0.001)
circle_y=np.sqrt(1-circle_x*circle_x)
plt.figure(figsize=(5,5))
plt.plot(circle_x,circle_y)

start_time=time.clock()

for i in range(0,N):
    score_x=np.random.rand()
    score_y=np.random.rand()

    if score_x*score_x+score_y*score_y<1:
        plt.scatter(score_x,score_y,marker='o',color='k')

        X=X+1
    else:
        plt.scatter(score_x,score_y,marker='o',color='b')
    pi=4*float(X)/float(N)

end_time=time.clock()
time=end_time-start_time
print(pi)
print(time)
plt.show()
