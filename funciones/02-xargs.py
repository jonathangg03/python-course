def suma(*numeros):  # With * numeros is going to be an iterable with all arguments we pass
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(1, 3, 65)
suma(5, 7, 3, 6, 2, 34, 5, 22)
suma(2, 1)
