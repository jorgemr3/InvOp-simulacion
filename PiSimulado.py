import random
dentro = 0
puntos = 10000000 # aumenta para mas exacto
for i in range(puntos):
    x, y = random.random(), random.random()
    if x**2 + y**2 <= 1:
        dentro+=1
var = 4*(dentro/puntos)
print("Pi es aproximadamente: ", var)



