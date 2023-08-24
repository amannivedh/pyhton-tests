import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,4.5,0.5)
print(x)

plt.figure(figsize=(12,5),dpi=300)
plt.plot(x[:6],x[:6]**2,'r^-')
plt.plot(x[5:],x[5:]**2,'g^--')
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("SIMPLE GRAPH",fontdict={'name':'Monotype Corsiva',
                                  'size':30,
                                  'color':"red",
                                  'weight':'bold'})
plt.legend(['First','second'],loc='lower right')
plt.xticks([0,1,2,3,4,5])
plt.yticks([0,4,8,12,16])
plt.show()