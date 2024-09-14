import numpy as np

array_1=np.array([1,1,1])
array_2=np.array([[1,1,1]])
print(array_1.shape)
print(array_2.shape)

print(array_2.ndim)
print(array_1.ndim)


arra_3=np.array([[1,2,3],[4,5,6]])
print(arra_3)


a=np.sin(np.pi/2) #radianos
print(a)

#soma

arr_4=np.array([[1,2,3]])
arr_5=np.array([[4,5,6]])
print(arr_4+arr_5)

arr_6=arr_4+5
print(arr_6)


#Multiplicação

print(arr_4*2)
print(arr_4*arr_5) #NÃO É UMA MULTIPLICAÇÃO MATRICIAL!

arr_7=np.array([[1,2,3],[4,5,6],[4,5,6]])

print(np.dot(arr_4,arr_7)) #MULTIPLICAÇÃO MATRICIAL


rodney=np.ones(8)*9
print(rodney)

olho=np.eye(5) #MATRIZ IDENTIDADE
print(olho)
print(olho.ndim)


arranjo=np.arange(0,8,2)
print(arranjo)

arranjo2=np.arange(6)
print(arranjo2)

linespaco=np.linspace(0,1,10)
print(linespaco)


c1=np.ones(8)
print(c1)
c1.reshape(2,4)
print(c1)
print(c1.reshape(2,4)) #não modifica só altera

c1.resize(2,4)#modifica o array
print(c1)


array12=np.array([[1,2,3],[4,3,6]])
array13=np.array([[8,2,3],[4,1,1]])
arra14=np.vstack((array12,array13))
print(arra14)