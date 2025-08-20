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

    
print("Programa 1")
print("Escribe 'Salir' para cerrar el programa")

while True:
    entrada = input("Escribe algo: ")
    if entrada.lower() == "salir":
        print("saliendo")
        break

    palabras = entrada.split()
    for palabra in palabras:
        resultado = clasificar(palabra)
        print(f"{palabra}: {resultado}")