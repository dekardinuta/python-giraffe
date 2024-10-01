# Dibujar un Triángulo en Python
=====================================

## Introducción al tema

En este ejemplo, aprenderás a utilizar una serie de instrucciones en Python para dibujar un triángulo en la pantalla. Utilizaremos declaraciones de impresión para crear la forma.

## Pasos para dibujar una forma

1. **Usar el comando `print("")`**: Utilizaremos este comando para imprimir cada línea de la forma.
2. **Repite el proceso**: Repetiremos el proceso tres veces para dibujar la forma.
3. **Crear la diagonal**: Empezaremos desde el último `print("/")` hasta el primero, dejando un espacio vacío en cada tramo, para darle forma de diagonal.
4. **Agregar la barra vertical**: Desde el `print("/")` de la línea 1 hasta el `print("")` de la línea 3, agregaremos una barra vertical `|` para que adopte la forma de un triángulo rectángulo.
5. **Cerrar la forma**: En la línea 4, agregaremos `print("/___|")` para cerrar la forma del triángulo.

### Explicación del código en app.py

* **Declaraciones de impresión**: Estas declaraciones imprimen información en la consola.
* **Orden de las instrucciones**: El orden en que escribimos las instrucciones es muy importante, ya que Python las ejecuta en orden.
* **Flexibilidad**: Podemos dibujar cualquier forma siempre que podamos especificar dentro de las declaraciones impresas.

### Ejemplos de uso

* **Dibujar un triángulo**: Utilizaremos el código proporcionado para dibujar un triángulo en la consola.
* **Crear otras formas**: Podemos utilizar las mismas técnicas para dibujar otras formas, como cuadrados, círculos, etc.

### Notas adicionales o recursos relacionados

* **Archivo app.py**: El archivo `app.py` contiene el código para dibujar el triángulo.
* **Código**:
```python
print("   /|")
print("  / |")
print(" /  |")
print("/___|")