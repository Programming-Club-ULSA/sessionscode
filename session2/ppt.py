import random

# Opciones posibles
opciones = ["piedra", "papel", "tijera"]

# Bienvenida e instrucciones
print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
print("Escribe tu elección: piedra, papel o tijera")

# Elección del jugador
jugador = input("¿Cuál eliges? ").lower()

# Validar entrada del jugador
if jugador not in opciones:
    print("Elección no válida, elige entre piedra, papel o tijera.")
else:
    # Elección de la computadora
    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")

    # Determinar el ganador
    if jugador == computadora:
        print("¡Es un empate!")
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")
