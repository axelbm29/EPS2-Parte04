# FUNCIONES
def mostrar_menu():
    print("Menu Opciones")
    print("\t" + "1. Registrar")
    print("\t" + "2. Eliminar")
    print("\t" + "3. Editar")
    print("\t" + "4. Listar")
    print("\t" + "5. Salir")
    
    
    
# FRONTEND
while True:
    mostrar_menu()
    opcion = input("Seleccione una opcion: ")
    print("\n")
    
    #isdigit() sirve para identificar si el string tiene solo numeros enteros positivos
    if opcion.isdigit() and 1 <= int(opcion) <= 5:
        opcion = int(opcion)
    else:
        print("\n\nOpción no válida. Por favor, seleccione una opción válida (1-5).")
        print("\n\n")
        continue
    
    if opcion == 1:
        print("Opcion 1")
    elif opcion == 2:
        print("Opcion 2")
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:
        print("Opcion 4")
    elif opcion == 5:
        print("Saliendo del programa.")
        break