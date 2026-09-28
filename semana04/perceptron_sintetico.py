from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Generar un dataset sintético de clasificación binaria
X, y = make_classification(
    n_samples=500,
    n_features=4,
    n_informative=3,
    n_redundant=0,
    random_state=42,
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

escalador = StandardScaler()
X_train = escalador.fit_transform(X_train)
X_test = escalador.transform(X_test)

print("X_train:", X_train.shape, " X_test:", X_test.shape)

from tensorflow import keras
from tensorflow.keras import layers

# 2. Definir la arquitectura: perceptrón multicapa (MLP)
modelo = keras.Sequential([
    layers.Input(shape=(4,)),               # 4 características de entrada
    layers.Dense(8, activation="relu"),    # capa oculta 1
    layers.Dense(4, activation="relu"),    # capa oculta 2
    layers.Dense(1, activation="sigmoid"), # salida: probabilidad de clase 1
])

modelo.summary()

# 3. Compilar: definir optimizador, función de pérdida y métricas
modelo.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)# 3. Compilar: definir optimizador, función de pérdida y métricas
modelo.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

import matplotlib
matplotlib.use("Agg")  # backend sin ventana gráfica, guarda directo a archivo
import matplotlib.pyplot as plt

# 4. Entrenar el modelo
historial = modelo.fit(
    X_train, y_train,
    epochs=30,
    batch_size=16,
    validation_split=0.2,
    verbose=1,
)

# 5. Graficar la evolución de la pérdida y la precisión
fig, ejes = plt.subplots(1, 2, figsize=(10, 4))

ejes[0].plot(historial.history["loss"], label="entrenamiento")
ejes[0].plot(historial.history["val_loss"], label="validación")
ejes[0].set_title("Pérdida (loss)")
ejes[0].set_xlabel("Época")
ejes[0].legend()

ejes[1].plot(historial.history["accuracy"], label="entrenamiento")
ejes[1].plot(historial.history["val_accuracy"], label="validación")
ejes[1].set_title("Precisión (accuracy)")
ejes[1].set_xlabel("Época")
ejes[1].legend()

plt.tight_layout()
plt.savefig("curvas_entrenamiento_sintetico.png", dpi=100)
print("\nGráfico guardado en curvas_entrenamiento_sintetico.png")

# 6. Evaluar el modelo en datos nunca vistos (conjunto de prueba)
perdida_test, precision_test = modelo.evaluate(X_test, y_test, verbose=0)
print(f"\nPérdida en test: {perdida_test:.4f}")
print(f"Precisión en test: {precision_test:.4f}")