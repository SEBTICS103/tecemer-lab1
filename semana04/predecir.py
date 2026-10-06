import numpy as np
from tensorflow import keras

# 1. Cargar el modelo entrenado en el Paso 3.4
modelo = keras.models.load_model("modelo_lluvia.keras")

# 2. Definir observaciones nuevas: [temp_max, temp_min, amplitud_termica]
# IMPORTANTE: deben escalarse con el MISMO escalador usado en el entrenamiento.
# Para esta demostración usamos valores ya aproximados a la escala estandarizada;
# en un flujo de producción real, se guardaría también el objeto StandardScaler (ver Nota).
observaciones_nuevas = np.array([
    [0.5, 0.3, 0.1],     # ejemplo: día con amplitud térmica moderada
    [-1.2, -0.8, -0.4],  # ejemplo: día con temperaturas bajas y poca amplitud
])

# 3. Predecir
probabilidades = modelo.predict(observaciones_nuevas)
predicciones = (probabilidades > 0.5).astype(int)

for i, (prob, pred) in enumerate(zip(probabilidades, predicciones)):
    etiqueta = "lluvioso" if pred[0] == 1 else "no lluvioso"
    print(f"Observación {i+1}: probabilidad={prob[0]:.3f} -> predicción: día {etiqueta}")