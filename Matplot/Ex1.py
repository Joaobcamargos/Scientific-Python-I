#Começando a entender o matplotlib
#Plotando uma circunfência a partir de 2 funções.
import matplotlib.pyplot as plt
import math
r=100
a=100
b=100

x = [x for x in range(2*r+1)] # range de 2*raio+1
y = [-math.sqrt(r**2-(y-a)**2)+b for y in x]
k = [math.sqrt(r**2-(y-a)**2)+b for y in x]


plt.plot(x, y)
plt.plot(x, k)
plt.show()
