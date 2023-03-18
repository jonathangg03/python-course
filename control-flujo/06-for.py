buscar = 10

for numero in range(5):  # range(5) return a secuence from 0 to 4
    # print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break  # break a loop for
else:  # In this case, else will be excecuted if we never pass for the break
    print('Numero no encontrado')

word = 'Hola mundo'
for letter in word:
    print(letter)

# Iterables: Lists, tuplas

# comando = ""
# while comando.lower() != "salir":
#     comando = input("$ ")


while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break

for i in range(5):
    for j in range(3):
        print(f"{i} {j}")
