
import pandas as pd
from pathlib import Path

# Proyecto RedConecta Telecom
# Ciencia de Datos - Semana 8

RUTA_BASE = Path(__file__).resolve().parent.parent
RUTA_DATASET = RUTA_BASE / "data" / "dataset_set_D_telecomunicaciones.xlsx"

INDICADORES = [
    "latencia_ms",
    "incidencias_reportadas",
    "tickets_soporte",
    "tiempo_resolucion_hr"
]


def cargar_datos(ruta=RUTA_DATASET):
    """Carga el dataset de telecomunicaciones."""
    return pd.read_excel(ruta)


def explorar_datos(df):
    """Muestra información general y calidad inicial del dataset."""
    print("Dimensiones del dataset:", df.shape)
    print("\nPrimeros cinco registros:")
    print(df.head())

    print("\nInformación de las columnas:")
    df.info()

    print("\nValores nulos por columna:")
    print(df.isnull().sum())

    print("\nEstadísticas descriptivas:")
    print(df.describe(include="all"))


def calcular_indicadores(df):
    """Calcula los promedios operacionales por región."""
    return df.groupby("region")[INDICADORES].mean().round(2)


def analizar_sla(df):
    """Calcula el cumplimiento de SLA por región."""
    return pd.crosstab(df["region"], df["cumplimiento_sla"])


if __name__ == "__main__":
    datos = cargar_datos()

    print("ANÁLISIS EXPLORATORIO - REDCONECTA TELECOM")
    explorar_datos(datos)

    print("\nIndicadores promedio por región:")
    print(calcular_indicadores(datos))

    print("\nCumplimiento de SLA por región:")
    print(analizar_sla(datos))

    print("\nAnálisis exploratorio finalizado correctamente.")
