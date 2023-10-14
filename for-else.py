#!/usr/bin/python3

#  meu metodo usando while #
from random import randint

dado = randint(1, 7)
numero = 0

while numero != dado:
    numero = randint(1, 7)
    if numero % 2 == 1:
        continue
    elif numero == dado:
        print('acertou', dado, numero)
    else:
        print('erro')
#######################################
print('#########')
#  metodo do curso


def dado():
    return randint(1, 6)


for dice in range(1, 7):
    if dice % 2 == 1:
        continue

    if dado() == dice:
        print('acerto', dice)
        break
else:
    print('erro')
