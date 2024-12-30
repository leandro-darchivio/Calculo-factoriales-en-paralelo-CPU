import sys
import time
from concurrent.futures import ProcessPoolExecutor

sys.set_int_max_str_digits(0)  # Establecer a 0 para desactivar el límite de dígitos

def partial_factorial(start, end):
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result

def factorial_parallel(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")

    num_workers = 12  # Usar todos los núcleos disponibles (ajustar según tu CPU)
    chunk_size = n // num_workers
    futures = []
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        for i in range(num_workers):
            start = i * chunk_size + 1
            end = (i + 1) * chunk_size if i < num_workers - 1 else n
            futures.append(executor.submit(partial_factorial, start, end))

    result = 1
    for future in futures:
        result *= future.result()
    return result

# Solicitar al usuario el número para el cual desea calcular el factorial
try:
    numero = int(input("Ingrese el número para calcular el factorial: "))

    if numero < 0:
        print("El número debe ser no negativo.")
    else:
        inicio = time.time()
        factorial_result = factorial_parallel(numero)
        num_digitos = len(str(factorial_result))
        fin = time.time()
        tiempo_total = fin - inicio

        print(f"Factorial de {numero} es {factorial_result}.")
        print(f"Tiene {num_digitos} dígitos.")
        print(f"Tiempo de cálculo: {tiempo_total:.5f} segundos.")

        nombre_archivo = f"{numero}.txt"
        with open(nombre_archivo, "w") as file:
            file.write(str(factorial_result))
        print(f"El resultado se ha guardado en el archivo {nombre_archivo}.")
except ValueError:
    print("Por favor, ingrese un número entero válido.")
