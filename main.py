from operaciones.basicas import suma
from operaciones.avanzadas import potencia
from operaciones.especiales import factorial

def menu_principal():
    print("\n=== CALCULADORA COLABORATIVA ===")
    print("1. Operaciones básicas")
    print("2. Operaciones avanzadas")
    print("3. Operaciones especiales")
    print("4. Programar es lo mas")
    print("5. Numero lindo o feo")
    print("6. Salir")

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
            print("programar es lo mas")
            
        elif opcion == 5:
	    a = input("Un numero:")
		if a == 6 or a == 2 or a == 10:
		    print("Tu numero es lindo")
		else:
		    print("Tu numero no es lindo")

    except ValueError:
        print("Error: Ingrese valores numéricos válidos")

if __name__ == "__main__":
    while True:
        menu_principal()
        if input("\n¿Continuar? (s/n): ").lower() != 's':
            break
