def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

texto = input("Ingresa un texto: ")
print(f"El texto tiene {contar_palabras(texto)} palabras.")
