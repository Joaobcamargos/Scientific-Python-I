import matplotlib.pyplot as plt
import numpy as np

fig ,ax = plt.subplots() #tupla de figura com eixos
x=np.linspace(0,2*np.pi,50)
y=np.sin(x)
plt.grid(True)
ax.plot(x,y,label='SENOIDE BACANA')
plt.legend()
ax.set_title('SENOIDE BACANISSIMO')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()