
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Proyecto RedConecta Telecom
# Ciencia de Datos - Semana 8

# 1. Definir rutas del proyecto
ruta_base = Path(__file__).resolve().parent.parent
ruta_dataset = ruta_base / "data" / "dataset_set_D_telecomunicaciones.xlsx"
ruta_dashboard = ruta_base / "dashboards"

ruta_dashboard.mkdir(parents=True, exist_ok=True)

# 2. Cargar el dataset
df = pd.read_excel(ruta_dataset)

# 3. Calcular indicadores promedio por región
indicadores = [
    "latencia_ms",
    "incidencias_reportadas",
    "tickets_soporte",
    "tiempo_resolucion_hr"
]

promedios = df.groupby("region")[indicadores].mean()

# 4. Crear dashboard de indicadores
fig, axes = plt.subplots(2, 2, figsize=(14, 9))

titulos = [
    "Latencia promedio por región",
    "Incidencias promedio por región",
    "Tickets de soporte por región",
    "Tiempo de resolución por región"
]

colores = ["skyblue", "salmon", "lightgreen", "orange"]

for ax, indicador, titulo, color in zip(
    axes.flat, indicadores, titulos, colores
):
    promedios[indicador].plot(
        kind="bar",
        ax=ax,
        color=color
    )
    ax.set_title(titulo)
    ax.set_xlabel("Región")
    ax.tick_params(axis="x", rotation=45)

axes[0, 0].set_ylabel("Latencia (ms)")
axes[0, 1].set_ylabel("Incidencias")
axes[1, 0].set_ylabel("Tickets")
axes[1, 1].set_ylabel("Horas")

plt.tight_layout()
plt.savefig(
    ruta_dashboard / "dashboard_redconecta.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# 5. Crear gráfico de cumplimiento SLA
tabla_sla = pd.crosstab(
    df["region"],
    df["cumplimiento_sla"]
)

ax = tabla_sla.plot(
    kind="bar",
    figsize=(10, 6),
    color=["salmon", "skyblue"]
)

ax.set_title("Cumplimiento de SLA por región")
ax.set_xlabel("Región")
ax.set_ylabel("Cantidad de registros")
ax.tick_params(axis="x", rotation=0)
ax.legend(title="Cumplimiento SLA")

plt.tight_layout()
plt.savefig(
    ruta_dashboard / "cumplimiento_sla_region.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

print("Gráficos generados correctamente:")
print("1. dashboard_redconecta.png")
print("2. cumplimiento_sla_region.png")
