"Módulo con funciones matematicas"


def resta_numeros(num_1: float, num_2: float) -> float:
    """
    Resta dos números y devuelve el resultado.

    Args:
        num_1 (float): El número del cual se va a restar.
        num_2 (float): El número que se va a restar de num_1.

    Returns:
        float: El resultado de la resta de num_1 menos num_2.
    """
    
    resultado = num_1 - num_2
    return resultado


def producto_numeros(num1: float, num2: float) -> float:
    """
    Multiplica dos números y devuelve el resultado.

    Args:
        num1 (float): Primer número a multiplicar.
        num2 (float): Segundo número a multiplicar.

    Returns:
        float: El resultado de la multiplicación de num1 y num2.
    """
    
    # Acá se realiza la multiplicación
    resultado = num1 * num2
    
    return resultado


def suma_numeros(num_1: float, num_2: float) -> float:
    """
    Suma dos números y devuelve el resultado.

    Args:
        num_1 (float): El primer número a sumar.
        num_2 (float): El segundo número a sumar.

    Returns:
        float: El resultado de la suma de num_1 y num_2.
    """
    
    resultado = num_1 + num_2
    return resultado


def suma_tres_numeros(num1: float, num2: float, num3: float) -> float:
    
    resultado_intermedio = suma_numeros(num1, num2)
    resultado_final = suma_numeros(resultado_intermedio, num3)
    
    return resultado_final
