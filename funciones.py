import sqlite3

def registrar_productos():
    print("Registro de Producto")
    codigo = input("Código: ")
    nombre = input("Nombre: ")
    precio = input("Precio: ")
    
    conexion = sqlite3.connect("BarzolaCamanCuro_almacen.db")
    cursor = conexion.cursor()
    consulta_insert = """INSERT INTO
                        producto (codigo, nombre, precio)
                        VALUES (?, ?, ?)
                    """
    cursor.execute(consulta_insert, (codigo, nombre, precio))
    
    conexion.commit()
    conexion.close()
    print("-"*25 + "\nProducto registrado\n" + "-"*25 + "\n\n")

def listar_productos():
    conexion = sqlite3.connect("BarzolaCamanCuro_almacen.db")
    cursor = conexion.cursor()

    consulta_select = """ SELECT codigo, nombre, precio
                        FROM producto
                      """
    cursor = conexion.cursor()
    cursor.execute(consulta_select)
    productos = cursor.fetchall()

    if productos:
        print("Lista de productos\n")
        print("Código\tNombre\tPrecio")
        for producto in productos:
            codigo, nombre, precio = producto
            print(f"{codigo}\t{nombre}\t{precio:.2f}")
    else:
        print("No hay productos registrados")

    conexion.close()
    print("\n\n")

def eliminar_productos():
    print("Eliminar productos por nombre")


def editar_productos():
    print("Editar Producto por nombre")