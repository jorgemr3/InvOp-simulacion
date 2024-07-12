file = open("cosas d matrices/matriz.txt", "r")
matriz = []
for linea in file:
    elem = linea.strip().split(",")
    for i in range(len(elem)):
        elem[i]=int(elem[i])
    matriz.append(elem)

n=len(matriz)
matrizt = [[j + 1 for j in range(n)] for _ in range(n)]
for k in range(n):
  for i in range(n):
      for j in range(n):
          if matriz[i][k] + matriz[k][j] < matriz[i][j]:
              matriz[i][j] = matriz[i][k] + matriz[k][j]
              matrizt[i][j] = k + 1

print("Matriz de pesos minimos")
for i in matriz:
    print(i)

print("Matriz de trayectorias minimas ")
for j in matrizt:
    print(j)
