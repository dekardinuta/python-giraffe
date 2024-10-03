# Creación de una calculadora básica

## Descripción
La finalidad de la creación de la calculadora es simplificar la operación aritmética de la suma. En este archivo, se utiliza la función `input()` de Python para obtener la entrada del usuario, y la función `print()` para imprimir el resultado en la consola.

## Funcionamiento
El funcionamiento de la calculadora se basa en la entrada de datos por parte del usuario. Se crean variables como `num1` y `num2` para almacenar los números ingresados, y `result` para almacenar el resultado de la suma.

Inicialmente, se utiliza la función `input()` para obtener los números ingresados por el usuario. Sin embargo, en Python, los números ingresados a través de `input()` se consideran cadenas de caracteres. Por lo tanto, al intentar sumar dos cadenas de caracteres, Python las concatena en lugar de sumar sus valores.

Para solucionar este problema, se utilizan las funciones `int()` y `float()` para convertir las cadenas de caracteres en números enteros y números flotantes, respectivamente. La función `int()` convierte las cadenas de caracteres en números enteros, permitiendo realizar operaciones aritméticas solo con enteros. La función `float()` convierte las cadenas de caracteres en números flotantes, permitiendo realizar operaciones aritméticas con números decimales.

Finalmente, se utiliza la función `print()` para imprimir el resultado de la suma en la consola.

