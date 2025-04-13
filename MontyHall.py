import random 

def monty_hall(cambio: bool) -> bool: 
    puertas = [1, 2, 3]

    # El Auto está detrás de una puerta aleatoria
    puerta_auto = random.choice(puertas)

    # El jugador elige una puerta aleatoria
    puerta_jugador = random.choice(puertas)

    # Monty abre una puerta que no tiene el auto y no es la elegida por el jugador
    puertas_monty = [puerta for puerta in puertas if puerta != puerta_jugador and puerta != puerta_auto]
    puerta_monty = random.choice(puertas_monty)

    # Si el jugador decide cambiar, elige la puerta que no ha sido abierta por Monty
    if cambio: 
        puerta_cambio = next(puerta for puerta in puertas if puerta != puerta_jugador and puerta != puerta_monty)
        puerta_final_jugador = puerta_cambio
    else:
        puerta_final_jugador = puerta_jugador 
    
    # El jugador gana si su puerta coincide con la puerta del auto
    gano = puerta_final_jugador == puerta_auto

    #Imprimimos los pasos realizados
    print("-" * 40)
    print("Resultados de la simulación:")
    print(f"Puerta del auto: {puerta_auto}")
    print(f"Puerta elegida por el jugador: {puerta_jugador}")
    print(f"Puerta abierta por Monty: {puerta_monty}")
    if cambio:
        print(f"Puerta elegida después de cambiar: {puerta_final_jugador}")
    else:
        print(f"El participante decide quedarse con su elección: {puerta_final_jugador}")
    print(f"El jugador {'ganó el auto!' if gano else 'no ganó'}.\n")

    print("-" * 40)
    return gano
    
#Simulamos una cambiando de puerta y otra sin cambiar - (Para solo una, se descomenta una de las dos)
#monty_hall(cambio=True)  # Cambia de puerta
#monty_hall(cambio=False) # No cambia de puerta



#Simulación Masiva
def simulacion_masiva(iteraciones: int, cambio: bool) -> int:
    ganados = 0
    for _ in range(iteraciones):
        if monty_hall(cambio):
            ganados += 1
    return ganados 




def menu_consola(): 
    print("Bienvenido al juego de Monty Hall")

    while True:
        print("¿Quieres cambiar de puerta?")
        print("1.Cambiar de puerta")
        print("2.No cambiar de puerta")
        respuesta = input("Seleccione una opción (1 o 2): ")
        
        if respuesta not in ('1', '2'):
            print("Opción no válida. Por favor, ingrese 1 o 2.")
            continue

        cambio = respuesta == '1'

        print("\n¿Qué desea hacer?")
        print("1. Jugar una sola vez")
        print("2. Simular múltiples partidas")
        accion = input("Seleccione una opción (1 o 2): ")

        if accion == "1":
            monty_hall(cambio)
        elif accion == "2":
            try:
                repeticiones = int(input("¿Cuántas partidas desea simular? (ej: 1000): "))
                ganadas = simulacion_masiva(repeticiones, cambio)
                print(f"\nResultado final: {ganadas} de {repeticiones} partidas ganadas.")
                print(f"Probabilidad empírica de ganar: {ganadas / repeticiones:.4f}\n")
            except ValueError:
                print("Número inválido. Intente de nuevo.\n")
        else:
            print("Opción inválida. Intente de nuevo.\n")

        otra = input("¿Desea volver al menú? (s/n): ").lower()
        if otra != "s":
            print("Gracias por usar el simulador.")
            break

# Iniciar el menú
if __name__ == "__main__":
    print("Bienvenido al simulador de Monty Hall")
    print("Este simulador te permitirá jugar el famoso juego de Monty Hall.")
    print("Puedes elegir cambiar o no cambiar de puerta y ver los resultados.")
    print("-" * 40)
    
    # Iniciar el menú de la consola
    menu_consola()