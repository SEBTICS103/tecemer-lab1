import datetime as dt
import pandas as pd
import requests

# Coordenadas de Huancayo
LATITUD, LONGITUD = -12.07, -75.21
DIAS_HISTORIAL = 90
DIAS_REZAGO = 5

fecha_fin = dt.date.today() - dt.timedelta(days=DIAS_REZAGO)
fecha_inicio = fecha_fin - dt.timedelta(days=DIAS_HISTORIAL)

url = "https://archive-api.open-meteo.com/v1/archive"
parametros = {
    "latitude": LATITUD,
    "longitude": LONGITUD,
    "start_date": fecha_inicio.isoformat(),
    "end_date": fecha_fin.isoformat(),
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "auto",
}

try:
    respuesta = requests.get(url, params=parametros, timeout=15)
    respuesta.raise_for_status()
except requests.exceptions.RequestException as error:
    print(f"No se pudo consultar la API histórica de Open-Meteo: {error}")
    raise SystemExit(1)

datos = respuesta.json()["daily"]
df_historico = pd.DataFrame({
    "fecha": datos["time"],
    "temp_max": datos["temperature_2m_max"],
    "temp_min": datos["temperature_2m_min"],
    "precipitacion": datos["precipitation_sum"],
})

# Sobrescribe el CSV con el historial ampliado
df_historico.to_csv("pronostico_huancayo.csv", index=False)

print(f"Rango consultado: {fecha_inicio} a {fecha_fin}")
print(f"Filas obtenidas: {len(df_historico)}")
print("\nArchivo pronostico_huancayo.csv actualizado con historial ampliado.")