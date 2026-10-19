
import matplotlib.pyplot as plt
from pathlib import Path

from analisis_exploratorio import (
    cargar_datos,
    calcular_indicadores,
    analizar_sla
)

# Proyecto RedConecta Telecom
# Ciencia de Datos - Semana 8

RUTA_BASE = Path(__file__).resolve().parent.parent
RUTA_DASHBOARD = RUTA_BASE / "dashboards"


def generar_dashboard(df):
    """Genera un dashboard de indicadores por región."""

    promedios = calcular_indicadores(df)

    indicadores = [
        "latencia_ms",
        "incidencias_reportadas",
        "tickets_soporte",
        "tiempo_resolucion_hr"
    ]

    titulos = [
        "Latencia promedio por región",
        "Incidencias promedio por región",
        "Tickets de soporte por región",
        "Tiempo de resolución por región"
    ]

    colores = ["skyblue", "salmon", "lightgreen", "orange"]

    fig, axes = plt.subplots(2, 2, figsize=(14, 9))

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

    RUTA_DASHBOARD.mkdir(parents=True, exist_ok=True)
    plt.savefig(
        RUTA_DASHBOARD / "dashboard_redconecta.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.close(fig)


def generar_grafico_sla(df):
    """Genera el gráfico de cumplimiento de SLA por región."""

    tabla_sla = analizar_sla(df)

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

    RUTA_DASHBOARD.mkdir(parents=True, exist_ok=True)
    plt.savefig(
        RUTA_DASHBOARD / "cumplimiento_sla_region.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.close(ax.figure)


if __name__ == "__main__":
    datos = cargar_datos()

    generar_dashboard(datos)
    generar_grafico_sla(datos)

    print("Gráficos generados correctamente:")
    print("1. dashboard_redconecta.png")
    print("2. cumplimiento_sla_region.png")
