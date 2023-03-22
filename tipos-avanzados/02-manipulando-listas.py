mascotas = ["wolfgang", "pelusa", "pulga", "copito"]
print(mascotas[0])
mascotas[0] = "bicho"  # Change a value of a list
print(mascotas)
print(mascotas[2:])  # Start from index 2
print(mascotas[-1])
# With negative index, if 0 is fst, -1 will go to the end of the list and so on
print(mascotas[1:2:2])
# Start from index 1, to index 2, and return each 2 elements (1, 3, 5..)

numeros = list(range(21))
print(numeros[::2])  # All numbers each 2 positions
print(numeros[1::2])  # Numbers from index 1 each 2 positions
