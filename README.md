# Cálculo de Factorial Paralelizado

Este proyecto permite calcular el factorial de un número de manera paralela utilizando el módulo `concurrent.futures` de Python para distribuir el trabajo entre varios procesos. Es especialmente útil cuando se calcula el factorial de números grandes, ya que aprovecha los recursos del CPU al dividir el trabajo en múltiples núcleos.


## Descripción

El código utiliza el módulo `concurrent.futures` de Python para dividir el cálculo del factorial en tareas que se ejecutan de manera concurrente en varios núcleos del procesador. Esto permite que el cálculo de grandes factoriales sea mucho más rápido que si se hiciera de manera secuencial.

## Cálculo de Números Extremadamente Grandes
Una de las características más poderosas de este proyecto es su capacidad para calcular factoriales de números muy grandes, incluso números casi infinitos. Al dividir el trabajo en varios procesos utilizando ProcessPoolExecutor, el cálculo se distribuye entre múltiples núcleos del procesador, lo que permite que el código maneje números de tamaño colosal sin que el sistema se quede sin recursos.

Debido a que Python maneja enteros arbitrariamente grandes (sin límite predefinido de tamaño), puedes calcular factoriales de números con cientos o incluso miles de dígitos. El límite práctico estará determinado por la memoria disponible en tu máquina y el tiempo de procesamiento, pero no hay un límite explícito en el código para el tamaño de los números.

Esto significa que, con los recursos adecuados, puedes calcular factoriales de números extremadamente grandes, lo que podría no ser posible con otros lenguajes que tengan restricciones en el tamaño de los enteros.


## Funcionalidad

1. **Cálculo del Factorial**: El factorial de un número `n` se calcula multiplicando todos los números enteros desde 1 hasta `n`. El factorial de `n` se denota como `n!`.
   
2. **Paralelización**: El cálculo se divide en `num_workers` (por defecto, 12) partes, y cada parte se ejecuta en paralelo utilizando un `ProcessPoolExecutor`. Esto distribuye el trabajo entre varios núcleos de la CPU, acelerando el proceso.

3. **Almacenamiento del Resultado**: El resultado del cálculo se guarda en un archivo de texto con el nombre del número cuyo factorial se calculó.

4. **Cálculo de los Dígitos**: Después de calcular el factorial, el código calcula cuántos dígitos tiene el resultado.

5. **Medición de Tiempo**: El tiempo total que tarda en calcular el factorial se mide y se muestra al final.

## Requisitos

Este proyecto requiere Python 3 y el módulo `concurrent.futures`, que está incluido en la biblioteca estándar de Python 3. 

## Uso

1. Clona o descarga este repositorio.
2. Ejecuta el script de Python.
3. Ingresa un número para calcular su factorial cuando se te solicite.
4. El resultado será mostrado en la consola y también guardado en un archivo de texto con el nombre del número ingresado.


