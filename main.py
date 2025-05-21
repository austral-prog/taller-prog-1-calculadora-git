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
            num = int(input('Ingrese un número entero: '))
            print(f'Resultado del doble: {num * 2}')
            #hola que tal 
            
    except ValueError:
        print("Error: Ingrese valores numéricos válidos")

if __name__ == "__main__":
    while True:
        menu_principal()
        if input("\n¿Continuar? (s/n): ").lower() != 's':
            break
