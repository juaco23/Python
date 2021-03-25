import random

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
dado4 = random.randint(1,6)

print("dado 1: %s"%dado1)
print("dado 2: %s"%dado2)
print("dado 3: %s"%dado3)
print("dado 4: %s"%dado4)


menor = min(dado1, dado2, dado3, dado4)
resultado  = dado1+ dado2 + dado3 + dado4 - menor
print(resultado)