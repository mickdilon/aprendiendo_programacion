def convertir_usd_a_mxn(cantidad, tasa_cambio=18.5):
    return cantidad * tasa_cambio

cantidad_usd = float(input("Ingresa la cantidad en USD: "))
print(f"{cantidad_usd} USD equivale a {convertir_usd_a_mxn(cantidad_usd):.2f} MXN")