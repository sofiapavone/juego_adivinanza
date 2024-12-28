import random

numero_secreto = random.randint(1,101)
adivinado = False
intentos = 0 
cant_max_intentos = 5 

print("Bienvenido al juego")

while not adivinado and intentos < cant_max_intentos:
    numero = int(input("Introduce un numero del 1 al 100: ")) #Lo casteamos porque si no devuelve un string

    if numero == numero_secreto:
        print("Adivinaste")
        adivinado = True
    elif numero > numero_secreto: 
        print("Debe ser menor")
    else:
        print("Debe ser mayor")
    intentos += 1 

if intentos == cant_max_intentos:
    print("Perdiste")