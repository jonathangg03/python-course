# It's like the spread operator in JS

lista1 = [1, 2, 3, 4]
lista2 = [5, 6]
lista3 = [*lista1, *lista2]
print(lista3)


punto1 = {"x": 19, "y": "hola"}
punto2 = {"y": 15}
nuevoPunto = {**punto1, **punto2, "z": "mundo"}  # with dictionaries
print(nuevoPunto)
# in this case y with hola is ignored, cause values are setted from right
