from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

driver_path = "C:\\Users\\libar\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
# Set the path to the Chrome WebDriver executable
chrome_options = Options()
chrome_options.binary_location = driver_path

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Configuración del WebDriver (ajusta la ruta al WebDriver según tu sistema)


# Abre WhatsApp Web
driver.get('https://web.whatsapp.com')

# Esperar a que el usuario escanee el código QR
input("Escanea el código QR y presiona Enter para continuar...")

def send_message(phone_number, message):
    # Buscar el contacto usando el número de teléfono
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.click()
    search_box.clear()
    search_box.send_keys(phone_number)
    search_box.send_keys(Keys.ENTER)
    
    time.sleep(5)  # Esperar a que se cargue el chat
    
    # Escribir y enviar el mensaje
    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="6"]')
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)

# Menú de opciones
def menu():
    print("\nMenu de Opciones")
    print("1. Enviar instantáneamente")
    print("2. Enviar programadamente")
    print("3. Salir")
    return int(input("Selecciona una opción: "))

# Pedir al usuario que ingrese el número de teléfono
phone_number = input("Por favor, ingresa el número de teléfono con el código de país (ejemplo: +34123456789): ")

# Pedir al usuario que ingrese el mensaje
message = input("Por favor, ingresa el mensaje que deseas enviar: ")

# Mostrar el menú
opcion = menu()

if opcion == 1:
    send_message(phone_number, message)
elif opcion == 2:
    hour = int(input("Por favor, ingresa la hora en formato 24 horas (ejemplo: 14 para las 2 PM): "))
    minute = int(input("Por favor, ingresa el minuto (ejemplo: 30): "))
    
    # Calcular el tiempo de espera hasta la hora programada
    current_time = time.localtime()
    target_time = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday, hour, minute, 0, 0, 0, -1))
    wait_time = time.mktime(target_time) - time.mktime(current_time)
    
    if wait_time > 0:
        print(f"Esperando {wait_time} segundos para enviar el mensaje...")
        time.sleep(wait_time)
        send_message(phone_number, message)
    else:
        print("La hora programada ya ha pasado. Por favor, intenta de nuevo.")
elif opcion == 3:
    print("Saliendo...")
    driver.quit()
else:
    print("Opción no válida")
    driver.quit()
