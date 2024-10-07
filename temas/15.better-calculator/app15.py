
# TODO: creacion de una mejor calculadora
num1 = float(input("Ingrese el primer numero: "))
op = input("Ingrese el operador aritmetico a usar: ")
num2 = float(input("Ingrese el segundo numero: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Operador aritmetico invalido")