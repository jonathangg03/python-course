def hola(nombre, apellido="Feliz"):  # Default values for parametters
    print("Hola mundo")
    print(f"Bienvenido {nombre} {apellido}")


hola("Jonathan", "García")
hola("Chanchito")
hola(apellido="Gonzalez", nombre="David")
# Named args, if we name one, all have to be named

# difference beetween paremetter and argument:
# what we use whem we define a function is a parametter
# when we call a funcition, the value we use inside of parentesis is an argument
