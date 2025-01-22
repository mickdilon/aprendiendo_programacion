import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

longitud = int(input("Ingresa la longitud de la contraseña: "))
print(f"Tu contraseña es: {generar_contraseña(longitud)}")
