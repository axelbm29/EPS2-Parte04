import sqlite3

def inicializar_base_datos():
    conexion = sqlite3.connect("BarzolaCamanCuro_almacen.db")
    cursor = conexion.cursor()
    tabla_productos = """
                    CREATE TABLE IF NOT EXISTS producto(
                      idproducto INTEGER PRIMARY KEY AUTOINCREMENT,
                      codigo TEXT,
                      nombre TEXT,
                      precio REAL
                    )
                    """
    cursor.execute(tabla_productos)
    conexion.commit()
    conexion.close()