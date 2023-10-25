from base_datos import inicializar_base_datos
from funciones import listar_productos, registrar_productos
def mostrar_menu():
    print("Menu Opciones")
    print("\t" + "1. Registrar")
    print("\t" + "2. Eliminar")
    print("\t" + "3. Editar")
    print("\t" + "4. Listar")
    print("\t" + "5. Salir")

if __name__ == "__main__":
    inicializar_base_datos()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")
        print("\n")

        if opcion.isdigit() and 1 <= int(opcion) <= 5:
            opcion = int(opcion)
        else:
            print("\n\nOpción no válida. Por favor, seleccione una opción válida (1-5).")
            print("\n\n")
            continue

        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            print("Saliendo del programa.")
            break