import requests

try:
    respuesta = requests.get("https://api.open-meteo.com/v1/forecast", timeout=5)
    respuesta.raise_for_status()
    print("Conexión exitosa a la API.")
except requests.exceptions.Timeout:
    print('La solicitud excedió el tiempo de espera.')
except requests.exceptions.RequestException as error:
    print(f'Error al consultar la API: {error}')