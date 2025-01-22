def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

opcion = input("Elige una conversión: 1) °C a °F, 2) °F a °C: ")

if opcion == '1':
    celsius = float(input("Ingresa la temperatura en °C: "))
    print(f"{celsius} °C son {celsius_a_fahrenheit(celsius):.2f} °F")
elif opcion == '2':
    fahrenheit = float(input("Ingresa la temperatura en °F: "))
    print(f"{fahrenheit} °F son {fahrenheit_a_celsius(fahrenheit):.2f} °C")
else:
    print("Opción no válida.")
