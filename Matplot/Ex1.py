#Começando a entender o matplotlib
#Plotando uma circunfência a partir de 2 funções.
import matplotlib.pyplot as plt
import math

x = [x for x in range(201)] # range de 2*raio+1
y = [-math.sqrt(10000-(y-100)**2)+100 for y in x]
k = [math.sqrt(10000-(y-100)**2)+100 for y in x]


plt.plot(x, y)
plt.plot(x, k)
plt.show()
