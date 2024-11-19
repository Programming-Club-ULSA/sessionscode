#!/usr/bin/env python3

# Importación de módulos
import sys
import os

# Definición de una función
def saludar(nombre):
    """
    Esta función recibe un nombre y muestra un saludo.
    """
    if not nombre:
        raise ValueError("El nombre no puede estar vacío.")
    print(f"¡Hola, {nombre}!")

# Definición de la función principal
def main():
    """
    Función principal del script. Lee un argumento de la línea de comandos
    y llama a la función saludar.
    """
    try:
        if len(sys.argv) > 1:
            # Llama a la función saludar con el argumento de la línea de comandos
            saludar(sys.argv[1])
        else:
            print("No se proporcionó un nombre en los argumentos.")
    except ValueError as e:
        print(f"Error: {e}")

# Bloque de ejecución principal
if __name__ == "__main__":
    main()
