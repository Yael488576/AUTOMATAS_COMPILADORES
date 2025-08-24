def es_entero(cadena):
    for c in cadena:
        if c < '0' or c > '9':
            return False
    return len(cadena) > 0

def es_palabra(cadena):
    for c in cadena:
        if not (('a' <= c <= 'z') or ('A' <= c <= 'Z')):
            return False
    return len(cadena) > 0

def es_compuesta(cadena):
    for c in cadena:
        if not (('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')):
            return False
    return len(cadena) > 0

def clasificar(cadena):
    if es_entero(cadena):
        return "Numero entero"
    elif es_palabra(cadena):
        return "Palabra"
    elif es_compuesta(cadena):
        return "Compuesta"

print("Programa 2")
print("Escribe 'Salir' para cerrar el programa")

total_palabras = 0
contador_enteros = 0
contador_palabras = 0
contador_compuestas = 0

while True:
    entrada = input("Escribe algo: ")
    if entrada.lower() == "salir":
        print("saliendo")
        break

    palabras = entrada.split()

    for palabra in palabras:
        resultado = clasificar(palabra)
        total_palabras += 1
        if resultado == "Numero entero":
            contador_enteros += 1
        elif resultado == "Palabra":
            contador_palabras += 1
        elif resultado == "Compuesta":
            contador_compuestas += 1


    print(f"Números enteros: {contador_enteros}")
    print(f"Palabras: {contador_palabras}")
    print(f"Compuestas: {contador_compuestas}")
    print()