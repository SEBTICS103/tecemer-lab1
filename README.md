# tecemer-lab1

# Laboratorio 01 - Fundamentos y Entornos de Desarrollo en Python

## Instalación

1. Crea el entorno virtual: `python -m venv .venv`
2. Activa el entorno: `.venv\Scripts\activate`
3. Instala el proyecto en modo editable: `pip install -e .`

## Uso

Ejecuta el script con:
`python -m tecemer_lab1.app`

o directamente:
`python src/tecemer_lab1/app.py`

## Estructura

- `src/`: Contiene el código fuente del paquete Python.
- `pyproject.toml`: Archivo de configuración del empaquetado del proyecto.
- `.gitignore`: Archivos y carpetas excluidos del control de versiones.

## Autor

Sebastian Huatuco Buendia — Tecnologías Emergentes - ISO46B


## Laboratorio 02 - Librerías para Datos y Automatización

### Flujo de Datos

* **Fuente**: Consumo de la API REST pública de [Open-Meteo](https://open-meteo.com/) (endpoint: `https://api.open-meteo.com/v1/forecast`), especificando las coordenadas de la ciudad de Huancayo (Latitud: `-12.07`, Longitud: `-75.21`) y un horizonte de pronóstico de 7 días.

* **Transformación**:
  * Computación vectorizada con [NumPy](https://numpy.org/) para operaciones sobre arreglos numéricos y estadística descriptiva, comparada frente al enfoque tradicional con bucles `for`.
  * Petición HTTP mediante la librería [requests](https://requests.readthedocs.io/), con manejo de `timeout` y captura de excepciones (`Timeout`, `RequestException`) para tolerar fallas de red.
  * Estructuración e inspección de claves de la respuesta JSON cruda (`daily`, `time`, `temperature_2m_max`, etc.) antes de su serialización.
  * Persistencia del JSON crudo (`pronostico_huancayo.json`) para trazabilidad del dato original, y construcción de la tabla inicial (`pronostico_huancayo.csv`) con el módulo estándar `csv`.
  * Carga y parseo del CSV mediante [pandas](https://pandas.pydata.org/), transformando la columna de fechas al tipo temporal `datetime64`.
  * Generación de características (*feature engineering*):
    * **Amplitud térmica**: Diferencia entre temperatura máxima y mínima (`temp_max - temp_min`).
    * **Flag de precipitación**: Clasificación booleana para identificar días lluviosos (`precipitacion > 0`).
    * **Categorización térmica**: Etiquetado condicional en `cálido` (>= 20°C), `templado` (>= 15°C) o `frío` (< 15°C).
  * Agregación estadística avanzada utilizando agrupamientos con `.groupby()` sobre las categorías térmicas.

* **Salida**: Generación del dataset estructurado [pronostico_huancayo_procesado.csv](./pronostico_huancayo_procesado.csv) y la tabla resumida [resumen_por_categoria.csv](./resumen_por_categoria.csv), a partir de los datos crudos [pronostico_huancayo.json](./pronostico_huancayo.json) y [pronostico_huancayo.csv](./pronostico_huancayo.csv).