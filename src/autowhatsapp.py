
import time

import pywhatkit as kit

# Pedir al usuario que ingrese el número de teléfono
phone_number = input("Por favor, ingresa el número de teléfono con el código de país (ejemplo: +34123456789): ")

# Pedir al usuario que ingrese el mensaje
message = input("Por favor, ingresa el mensaje que deseas enviar: ")

# Menú de opciones
def menu():
    print("\nMenu de Opciones")
    print("1. Enviar instantáneamente")
    print("2. Enviar programadamente")
    print("3. Salir")
    return int(input("Selecciona una opción: "))

# Lógica del menú
opcion = menu()

if opcion == 1:
    # Enviar instantáneamente
    for i in range(10):
        kit.sendwhatmsg_instantly(phone_number, message)
        time.sleep(10)
elif opcion == 2:
    # Enviar programadamente
    hour = int(input("Por favor, ingresa la hora en formato 24 horas (ejemplo: 14 para las 2 PM): "))
    minute = int(input("Por favor, ingresa el minuto (ejemplo: 30): "))
    kit.sendwhatmsg(phone_number, message, hour, minute)
elif opcion == 3:
    print("Saliendo...")
    exit()
else:
    print("Opción no válida")

