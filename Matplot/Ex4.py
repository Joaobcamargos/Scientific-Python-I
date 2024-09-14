import matplotlib.pyplot as plt
import numpy as np

fig ,ax = plt.subplots() #tupla de figura com eixos
x=np.linspace(0,2*np.pi,50)
y=np.sin(x)
plt.grid(True)
ax.plot(x,y)
plt.show()