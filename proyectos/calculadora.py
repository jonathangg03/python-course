n1 = input('Escribe el primer numero ')
n2 = input('Escribe el segundo numero ')

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
mult = n1 * n2
div = n1 / n2

mensaje = f"""
Con los numeros entregados: {n1} y {n2}:
La suma es: {suma}
La resta es: {resta}
La multiplicación es: {mult}
La división es: {div}
"""

print(mensaje)
