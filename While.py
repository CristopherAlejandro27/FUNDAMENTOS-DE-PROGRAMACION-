def mostrar_menu() -> None:
    print("\n===== MENÚ PRINCIPAL =====")
    print("1) Saludar")
    print("2) Calcular la suma de dos números")
    print("3) Mostrar la tabla de multiplicar del 5")
    print("0) Salir")
    

def opcion_saludar() -> None:
    nombre = input("¿Cómo te llamas? ").strip()
    print(f"¡Hola, {nombre}! Bienvenido/a.")


def opcion_suma() -> None:
    try:
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        print(f"La suma es: {a + b}")
    except ValueError:
        print(" Debes introducir valores numéricos.")


def opcion_tabla() -> None:
    numero = 5
    print(f"\nTabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} × {i} = {numero * i}")


#Esta función (while) sirve para ejecutar un solo bloque de código.  
# ---------- Bucle principal ----------
continuar = True              
while continuar:
    mostrar_menu()             
    eleccion = input("Elige una opción: ").strip()
#La variable continuar sirve continuar mientras sea True y darle fin cuando la variable de False y termine.
    if eleccion == "1":
        opcion_saludar()
        #Saluda al usuario. 
    elif eleccion == "2":
        opcion_suma()
        #Hace suma con los numeros que se le dan y te entrega el resultado.
    elif eleccion == "3":
        opcion_tabla()
        #Multuplica los numeros que se le dan y te da el resultado.
    elif eleccion == "0":
        print("\n ¡Hasta luego!")
        #Se detiene.
        continuar = False
    else:
        print(" Opción no válida, intenta de nuevo.")

print("Programa terminado.")