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
            print("Suma 1, resta 2") 
            var = int(input("Queres hacer suma o resta ?: "))
            if var == 1:
                a = float(input("Ingrese primer número: "))
                b = float(input("Ingrese segundo número: "))
                print(f"Resultado suma: {suma(a, b)}")
            else:
                a = float(input("Ingrese primer numero : "))
                b = float(input("Ingrese segundo numero ; "))
                c = a - b
                print(f"Resultado de la resta es igual a: {c}")
        elif opcion == 2:
            base = float(input("Ingrese base: "))
            exponente = float(input("Ingrese exponente: "))
            print(f"Resultado potencia: {potencia(base, exponente)}")
            
        elif opcion == 3:
            num = int(input("Ingrese número entero: "))
            print(f"Factorial: {factorial(num)}")
            
    except ValueError:
        print("Error: Ingrese valores numéricos válidos")

if __name__ == "__main__":
    while True:
        menu_principal()
        if input("\n¿Continuar? (s/n): ").lower() != 's':
            break
