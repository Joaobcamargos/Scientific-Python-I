import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,4*np.pi,500)
y=np.sin(x)
y_2=np.sin(2*x)
plt.plot(x,y)
plt.plot(x,y_2)
plt.xlabel('EIXO X')
plt.ylabel('EIXO Y')
plt.grid(True)



plt.show()
