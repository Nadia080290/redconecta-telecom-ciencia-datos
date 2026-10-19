
import pandas as pd
from pathlib import Path

# Proyecto RedConecta Telecom
# Ciencia de Datos - Semana 8

# 1. Definir la ubicación del dataset
ruta_base = Path(__file__).resolve().parent.parent
ruta_dataset = ruta_base / "data" / "dataset_set_D_telecomunicaciones.xlsx"

# 2. Cargar los datos
df = pd.read_excel(ruta_dataset)

# 3. Mostrar información general
print("ANÁLISIS EXPLORATORIO - REDCONECTA TELECOM")
print("=" * 50)

print("\nDimensiones del dataset:")
print(df.shape)

print("\nPrimeros cinco registros:")
print(df.head())

print("\nInformación de las columnas:")
df.info()

# 4. Identificar valores faltantes
print("\nValores nulos por columna:")
print(df.isnull().sum())

# 5. Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(df.describe(include="all"))

# 6. Analizar indicadores por región
indicadores = [
    "latencia_ms",
    "incidencias_reportadas",
    "tickets_soporte",
    "tiempo_resolucion_hr"
]

print("\nIndicadores promedio por región:")
print(df.groupby("region")[indicadores].mean().round(2))

# 7. Analizar cumplimiento del SLA
print("\nCumplimiento de SLA por región:")
print(pd.crosstab(df["region"], df["cumplimiento_sla"]))

print("\nAnálisis exploratorio finalizado correctamente.")
