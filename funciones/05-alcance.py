saludo = "Hola global"


def saludar():
    saludo = "Hola mundo"


def saludaChanchito():
    global saludo
    saludo = "Hola chancito"


saludar()
saludaChanchito()

# When there are 2 variables with the same name in diferent context, both are saved in different memory space
# It's a bad practice to use global variables
# If we want to use them, we need to use the word global [variable] at the begining of that function
