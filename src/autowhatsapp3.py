import pyautogui, webbrowser
from time import sleep


# Pedir al usuario que ingrese el número de teléfono
phone_number = input("Por favor, ingresa el número de teléfono con el código de país (ejemplo: +34123456789): ")
# Pedir al usuario que ingrese el mensaje
message = input("Por favor, ingresa el mensaje que deseas enviar: ")
# Cantidad de veces a enviar el mensaje
repetir = int(input("Cuantas veces queres enviarle el mensaje?: "))

# Abrir el navegador de WhatsApp Web
webbrowser.open('https://web.whatsapp.com/send?phone='+phone_number)
# Esperar 15 segundos antes de enviar el mensaje
sleep(15)




for i in range(repetir):
    pyautogui.typewrite(message) # Escribir el mensaje
    pyautogui.press('enter') # Enviar el mensaje
