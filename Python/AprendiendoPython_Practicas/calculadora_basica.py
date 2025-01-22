def calculadora():
    print("Operaciones: suma (+), resta (-), multiplicación (*), división (/)")
    num1 = float(input("Ingresa el primer número: "))
    operacion = input("Ingresa la operación: ")
    num2 = float(input("Ingresa el segundo número: "))

    if operacion == '+':
        print(f"Resultado: {num1 + num2}")
    elif operacion == '-':
        print(f"Resultado: {num1 - num2}")
    elif operacion == '*':
        print(f"Resultado: {num1 * num2}")
    elif operacion == '/':
        if num2 != 0:
            print(f"Resultado: {num1 / num2}")
        else:
            print("Error: División entre cero.")
    else:
        print("Operación no válida.")

calculadora()
