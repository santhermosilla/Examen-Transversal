#Diccionarios que serán utilizados en el programa.
#Diccionario de productos.
productos = {'M001': ['Alimento Premium', 'comida', 'DogPlus', 10, True,
False],
'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False,
False],
'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False,
True],
'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True,
False],
'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False,
False],}
#Diccionario de stock.
stock = {'M001': [32990, 12],
'M002': [9990, 0],
'M003': [5490, 25],
'M004': [7990, 5],
'M005': [11990, 7],
'M006': [24990, 3]}

#Funcion para leer la opción elegida en el menú principal.
def leer_opcion():
    try:
        opcion = int(input("Su opción: "))
    except:
        print("Debe elegir una opción válida.")
    else:
        if opcion < 1 or opcion > 6:
            print("Debe elegir una opción válida.")
        else:
            return opcion

#Función de busqueda para unidades por categoría de productos.
def unidades_categoria(x, dic_prod, dic_stock):
    total_stock = 0
    for clave, valor in dic_prod.items():
        if valor[1] == x:
            total_stock += dic_stock[clave][1]
    print(f"El stock total en la categoria {x} es: {total_stock}.")

#Función para busqueda de productos según un rango de precio dado por el usuario.
def busqueda_precio(min, max, dic_prod, dic_stock):
    lista_productos = []
    for clave, valor in dic_stock.items():
        if min < valor[0] < max and valor[1] > 0:
            producto_añadir = dic_prod[clave][0] + "--" + clave
            lista_productos.append(producto_añadir)
    if len(lista_productos) == 0:
        print("No hay productos en ese rango de precios.")
    else:
        lista_ordenada = sorted(lista_productos)
        print(lista_ordenada)


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
    if opcion == 1:
        categoria = input("Indique la categoría a buscar: ").lower().strip()
        unidades_categoria(categoria, productos, stock)
    elif opcion == 2:
        while True:
            try:
                p_min = int(input("Ingrese el valor mínimo: "))
                p_max = int(input("Ingrese el valor máximo: "))
            except:
                print("Debe ingresar valores enteros.")
            else:
                if p_min < 0 or p_max < 0 or p_min > p_max:
                    print("Debe ingresar un rango de valores válido.")
                    continue
                else:
                    busqueda_precio(p_min,p_max,productos,stock)
                    break