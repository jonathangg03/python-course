numeros = [1, 2, 3]
numeros_b = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# bad practice
# primero = numero[0]
# segundo = numero[1]
# tercero = numero[2]

primero, segundo, tercero = numeros

# primero, segundo = numeros You can't let undesestructured values

primero, *otros = numeros
print(otros)

# otros will be an iterable with the rest of the numbers
primero, segundo, *otros, penu, ultimo = numeros_b

print(primero, segundo, penu, ultimo)
