import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

opciones = [rock, paper, scissors]

print("""
Elegí:
0 - Piedra
1 - Papel
2 - Tijera
""")

eleccion_jugador = -1
while eleccion_jugador not in [0, 1, 2]:
    try:
        eleccion_jugador = int(input())
    except ValueError:
        print("Ingresar una opción válida.")
    
eleccion_computadora = random.choice([0, 1, 2])

print(opciones[eleccion_jugador])
print("Elección de la computadora:")
print(opciones[eleccion_computadora])

if (eleccion_jugador - eleccion_computadora) == 0:
    print("Empate.")
elif (eleccion_jugador - eleccion_computadora) == 1 or\
     (eleccion_jugador - eleccion_computadora) == -2:
    print("Vos ganaste.")
else:
    print("La computadora ganó.")