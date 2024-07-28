import matplotlib.pyplot as plt
import math
#Plotando uma elipse a partir de 2 funções.


h = 100
k = 100
a = 150
b = 100

x = [i for i in range(h - a, h + a + 1)]#    [h - a, h + a]
y = [k + math.sqrt(b**2 * (1 - ((xi - h)**2 / a**2))) for xi in x]
k = [k - math.sqrt(b**2 * (1 - ((xi - h)**2 / a**2))) for xi in x]

plt.plot(x, y)
plt.plot(x, k)

plt.show()
