import pandas as pd

df = pd.read_csv("pronostico_huancayo.csv")
n_lluvioso = (df["precipitacion"] > 0).sum()
n_no_lluvioso = (df["precipitacion"] == 0).sum()

print(f"Total de filas: {len(df)}")
print(f"Días lluviosos: {n_lluvioso} | Días no lluviosos: {n_no_lluvioso}")

assert len(df) >= 30, "Muy pocas filas; aumenta DIAS_HISTORIAL en ampliar_dataset.py"
assert (
    n_lluvioso >= 5 and n_no_lluvioso >= 5
), "Alguna clase tiene muy pocos casos; amplía el rango de fechas"

print("Dataset ampliado validado correctamente.")