import numpy as np
import matplotlib.pyplot as plt
data=[[30,25,50,20],[40,23,50,17],[35,22,45,19]]
x=np.arange(1,5)
print(x)
fig=plt.figure()

plt.bar(x+0.00,data[0],color='b',width=0.25)
plt.bar(x+0.25,data[1],color='g',width=0.25)
plt.bar(x+0.50,data[2],color='r',width=0.25)
plt.show()