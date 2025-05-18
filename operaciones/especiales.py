def factorial(n: int) -> int:
    """
    Calcula el factorial de un número entero positivo
    
    Args:
        n (int): Número entero
    
    Returns:
        int: n!
    
    Raises:
        ValueError: Si n es negativo
    """
    if n < 0:
        raise ValueError("Factorial no definido para negativos")
    return 1 if n == 0 else n * factorial(n - 1)

# Espacio para funciones trigonométricas, estadísticas, etc.
