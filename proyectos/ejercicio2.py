
print("""
      Bienvenido a la calculadora.
      Las operaciones permitidas son suma, resta, mult y div
      """)
# My solution
numero_a = 0
numero_b = 0
resultado = 0
op = 0

while numero_a == 0:
    numero_a = input("Ingrese un numero a ")
    numero_a = int(numero_a)


while True:
    op = input("Ingrese una operación ")
    if op.lower() == 'salir':
        break
    numero_b = input("Ingrese un numero b ")
    if numero_b.lower() == 'salir':
        break
    numero_b = int(numero_b)

    if op.lower() == "suma":
        numero_a += numero_b
        print(numero_a)

    if op.lower() == "resta":
        numero_a -= numero_b
        print(numero_a)

    if op.lower() == "mult":
        numero_a *= numero_b
        print(numero_a)

    if op.lower() == "div":
        numero_a /= numero_b
        print(numero_a)

# Teacher's solution

resultado = ""

while True:
    if not resultado:
        resultado = input("Ingrese número: ")
        if resultado.lower() == 'salir':
            break
        resultado = int(resultado)

    op = input("Ingrese operación: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)
    if op.lower() == "suma":
        resultado += n2

    if op.lower() == "resta":
        resultado -= n2

    if op.lower() == "mult":
        resultado *= n2

    if op.lower() == "div":
        resultado /= n2

    print(resultado)
