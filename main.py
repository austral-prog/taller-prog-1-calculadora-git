from operaciones.basicas import suma
from operaciones.avanzadas import potencia
from operaciones.especiales import factorial

def menu_principal():
    print("\n=== CALCULADORA COLABORATIVA ===")
    print("1. Operaciones básicas")
    print("2. Operaciones avanzadas")
    print("3. Operaciones especiales")
    print("4. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            a = float(input("Ingrese primer número: "))
            b = float(input("Ingrese segundo número: "))
            print(f"Resultado suma: {suma(a, b)}")
            
        elif opcion == 2:
            base = float(input("Ingrese base: "))
            exponente = float(input("Ingrese exponente: "))
            print(f"Resultado potencia: {potencia(base, exponente)}")
            
        elif opcion == 3:
            num = int(input("Ingrese número entero: "))
            print(f"Factorial: {factorial(num)}")

        elif opcion == 4:
<<<<<<< HEAD
            a = int(input("Ingrese su número: "))
            b = int(input("Ingrese su número: "))
            if (a-b) > 0:
                print(f"Su número es positivo")
            else:
                print(f"Su número es negativo")
                
        elif opcion == 5:    
            print("programar es lo mas")
            
>>>>>>> c7eeb24349894d5c957386bf79b5b2b224f5e6ac
    except ValueError:
        print("Error: Ingrese valores numéricos válidos")

if __name__ == "__main__":
    while True:
        menu_principal()
        if input("\n¿Continuar? (s/n): ").lower() != 's':
            break
