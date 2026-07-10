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
        if min <= valor[0] <= max and valor[1] > 0:
            producto_añadir = dic_prod[clave][0] + "--" + clave
            lista_productos.append(producto_añadir)
    if len(lista_productos) == 0:
        print("No hay productos en ese rango de precios.")
    else:
        lista_ordenada = sorted(lista_productos)
        print(f"Los productos encontrados son: {lista_ordenada}")

#Función de verificación de código.
def buscar_codigo(x, dic_prod):
    for clave in dic_prod.keys():
        if x == clave:
            return True
    return False

#Función para cambio de precio.
def actualizar_precio(x, valor, dic_prod):
    if buscar_codigo(x, dic_prod):
        stock[x][0] = valor
        return True
    return False

#Funciones de verificacion para cada dato en funcionalidad agregar producto: 
def ver_codigo(x, dic_prod):
    if buscar_codigo(x, dic_prod) or x.isspace() or x == "":
        return False
    return True
def ver_nombre(x):
    if x.isspace() or x == "":
        return False
    return True
def ver_categoria(x):
    if x.isspace() or x == "":
        return False
    return True
def ver_marca(x):
    if x.isspace() or x == "":
        return False
    return True
def ver_peso(x):
    try:
        x = float(x)
        if x > 0:
            return True
        else:
            return False
    except:
        return False
def ver_importado(x):
    if x == "s":
        x == True
    else:
        x == False
def ver_cachorro(x):
    if x == "s":
        x == True
    else:
        x == False
def ver_precio(x):
    try:
        x = int(x)
        if x > 0:
            return True
        else:
            return False
    except:
        return False
def ver_unidades(x):
    try:
        x = int(x)
        if x >= 0:
            return True
        else:
            return False
    except:
        return False

#Funcion para agregar producto.
def agregar_producto(codigo,nombre,categoria,marca,peso_kg,es_importado,es_para_cachorro,precio,unidades):
    productos[codigo] = [nombre, categoria,marca,float(peso_kg),es_importado,es_para_cachorro]
    stock[codigo] = [int(precio),int(unidades)]
    return True
#Funcion para eliminar producto
def eliminar_producto(x, dic_prod):
    if buscar_codigo(x,dic_prod):
        del productos[x]
        del stock[x]
        return True
    else:
        return False
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
    elif opcion == 3:
        while True:
            cod_buscar = input("Ingrese código de producto a actualizar: ").upper()
            try:
                nuevo_precio = int(input("Ingrese el nuevo precio a asignar: "))
            except:
                print("Debe ingresar un precio válido.")
                continue
            else:
                if actualizar_precio(cod_buscar, nuevo_precio, productos):
                    print("Precio actualizado.")
                else:
                    print("El código no existe.")
                seguir = input("¿Desea actualizar otro precio (s/n)?: ")
                if seguir == "s":
                    continue
                else:
                    break
    elif opcion == 4:
        codigo = input("Ingrese el código: ").upper().strip()
        nombre = input("Ingrese el nombre: ")
        categoria = input("Ingrese la categoría: ")
        marca = input("Ingrese la marca: ")
        peso_kg = input("Ingrese el peso en kg: ")
        es_importado = input("¿Es importado?(s/n): ")
        es_para_cachorro = input("¿Es para cachorro?(s/n): ")
        precio = input("Ingrese el precio: ")
        unidades = input("Ingrese las unidades: ")
        if not ver_codigo(codigo, productos) or not ver_nombre(nombre) or not ver_categoria(categoria) or not ver_marca(marca) or not ver_peso(peso_kg) or not ver_precio(precio) or not ver_unidades(unidades):
            print("El codigo ya existe o un dato no fue ingresado correctamente")
        else:
            if agregar_producto(codigo,nombre,categoria,marca,peso_kg,es_importado,es_para_cachorro,precio,unidades):
                print("Producto agregado.")
    elif opcion == 5:
        cod_eliminar = input("Ingrese el código del producto a eliminar: ").strip().upper()
        if eliminar_producto(cod_eliminar,productos):
            print("Producto eliminado.")
        else:
            print("El codigo no existe.")
    elif opcion == 6:
        print("Programa finalizado.")
        break