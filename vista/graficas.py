"""Capa de vista: grafica de la practica."""

import matplotlib.pyplot as plt

from datos.datos_clima import UMBRALES


class Graficas:

    # -----------------------------
    # Gráfica para las practicas
    # -----------------------------
    def indice_por_hora(self, original, ajustado):
        horas = [r["hora"] for r in original]

        plt.figure(figsize=(10, 5))
        plt.plot(horas, [r["indice"] for r in original], label="Modelo original")
        plt.plot(horas, [r["indice"] for r in ajustado], label="Modelo ajustado")
        for limite in UMBRALES:
            plt.axhline(
                y=limite,
                linestyle="--",
                label=f"Límite {limite}"
            )
        plt.xlabel("Hora")
        plt.ylabel("Índice de lluvia")
        plt.title("Índice de lluvia durante el día")
        plt.grid(True)
        plt.legend()

        plt.show()
