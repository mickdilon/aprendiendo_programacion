# Codigo que es para uso de aprendizaje, asi como para conocer la secuencia de fibonacci en el lenguaje de programacion Python,
# si hay alguna duda, favor de escribir a Miguel Angel Garcia Cambron <inggmiguelangelgc@gmail.com>

def fibonacci(n):
    """Genera la secuencia de Fibonacci hasta n elementos."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence


# Solicitar la entrada del usuario
try:
    num = int(input("¿Cuántos números de la secuencia de Fibonacci deseas generar? "))
    if num <= 0:
        print("Por favor, ingresa un número positivo.")
    else:
        result = fibonacci(num)
        print(f"Secuencia de Fibonacci con {num} elementos:")
        print(", ".join(map(str, result)))
except ValueError:
    print("Por favor, ingresa un número válido.")
