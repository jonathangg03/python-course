def get_product(**datos):  # Are defined by **
    print(datos)
    # we access to keywords by the mame of a key
    print(datos["id"], datos["name"])


get_product(id="23", name="iphone", desc="Esto es un iphone")
# we can pass as many args as we want, but in an order keyword= value
