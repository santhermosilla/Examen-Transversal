#Diccionarios que serán utilizados en el programa.
#Diccionario de productos.
productos = {}
#Diccionario de stock.
stock = {}

#Funcion para leer la opción elegida en el menú principal.
def leer_opcion():
    try:
        opcion = int(input("Su opción: "))
    except:
        print("Debe elegir una opción válida")
    else:
        if opcion < 1 or opcion > 6:
            print("Debe elegir una opción válida")
        else:
            return opcion

    
while True:
# String para imprimir como menú.
    menu = '''========== MENÚ PRINCIPAL ==========
1. Unidades por categoría
2. Búsqueda de productos por rango de precio
3. Actualizar precio de producto
4. Agregar producto
5. Eliminar producto
6. Salir
=====================================
    '''
    print(menu)
    opcion = leer_opcion()