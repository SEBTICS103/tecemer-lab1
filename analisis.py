import pandas as pd

df = pd.read_csv("pronostico_huancayo.csv")
df["fecha"] = pd.to_datetime(df["fecha"])
print(df.head())
print(df.info())

df["amplitud_termica"] = df["temp_max"] - df["temp_min"]
df["dia_lluvioso"] = df["precipitacion"] > 0
df["categoria"] = df["temp_max"].apply(
    lambda t: "cálido" if t >= 20 else ("templado" if t >= 15 else "frío")
)

print(df)
print(df.describe())

resumen = df.groupby("categoria").agg(
    dias=("categoria", "count"),
    temp_max_promedio=("temp_max", "mean"),
    precipitacion_total=("precipitacion", "sum"),
)
print(resumen)

df.to_csv("pronostico_huancayo_procesado.csv", index=False)
resumen.to_csv("resumen_por_categoria.csv")