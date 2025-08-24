import re

def leer_archivo(nombre_archivo):
    """Lee el contenido de un archivo de texto"""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'")
        return None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def clasificar_lexemas(texto):
    """Clasifica los lexemas en palabras, números y combinadas"""
    # Dividir el texto en lexemas (separados por espacios)
    lexemas = texto.split()
    
    # Inicializar contadores
    contador_palabras = 0
    contador_numeros = 0
    contador_combinadas = 0
    
    # Listas para almacenar los lexemas clasificados
    palabras = []
    numeros = []
    combinadas = []
    
    # Recorrer cada lexema y clasificarlo
    for lexema in lexemas:
        # Verificar si es solo letras (palabra)
        if re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+$', lexema):
            contador_palabras += 1
            palabras.append(lexema)
        # Verificar si es solo números
        elif re.match(r'^\d+$', lexema):
            contador_numeros += 1
            numeros.append(lexema)
        # Verificar si es combinación de letras y números
        elif re.match(r'^[a-zA-Z]+\d+$|^\d+[a-zA-Z]+$|^[a-zA-Z]+\d+[a-zA-Z]*$|^\d+[a-zA-Z]+\d*$', lexema):
            contador_combinadas += 1
            combinadas.append(lexema)
    
    return {
        'total_lexemas': len(lexemas),
        'palabras': contador_palabras,
        'numeros': contador_numeros,
        'combinadas': contador_combinadas,
        'lista_palabras': palabras,
        'lista_numeros': numeros,
        'lista_combinadas': combinadas
    }

def main():
    # Nombre del archivo a procesar
    nombre_archivo = "Texto Programa.txt"  # Puedes cambiar esto por tu archivo
    
    # Leer el archivo
    contenido = leer_archivo(nombre_archivo)
    if contenido is None:
        return
    
    # Contar caracteres
    total_caracteres_con_espacios = len(contenido)
    total_caracteres_sin_espacios = len(contenido.replace(' ', ''))
    
    # Clasificar lexemas
    resultado = clasificar_lexemas(contenido)
    
    # Mostrar resultados
    print("=" * 50)
    print("RESULTADOS DE CLASIFICACIÓN DE LEXEMAS")
    print("=" * 50)
    print(f"Total de caracteres (con espacios): {total_caracteres_con_espacios}")
    print(f"Total de caracteres (sin espacios): {total_caracteres_sin_espacios}")
    print(f"Total de lexemas: {resultado['total_lexemas']}")
    print(f"Total de palabras: {resultado['palabras']}")
    print(f"Total de números: {resultado['numeros']}")
    print(f"Total de combinadas: {resultado['combinadas']}")
    
    # Mostrar detalles si se desea
    print("\nDetalles:")
    print(f"Palabras: {', '.join(resultado['lista_palabras'])}")
    print(f"Números: {', '.join(resultado['lista_numeros'])}")
    print(f"Combinadas: {', '.join(resultado['lista_combinadas'])}")

if __name__ == "__main__":
    main()