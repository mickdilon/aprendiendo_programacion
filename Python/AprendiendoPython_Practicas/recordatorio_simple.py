import time

def recordatorio(mensaje, tiempo):
    print(f"Esperando {tiempo} segundos...")
    time.sleep(tiempo)
    print(f"¡Recordatorio! {mensaje}")

mensaje = input("¿Cuál es el recordatorio?: ")
tiempo = int(input("¿En cuántos segundos quieres recordarlo?: "))
recordatorio(mensaje, tiempo)