"""Practica 01 - Simulacion: construccion y simulacion de un modelo matematico."""

from datos.datos_clima import PESOS_AJUSTADOS, PESOS_ORIGINALES, REGISTROS
from logica.modelo_lluvia import simular
from vista.graficas import Graficas
from vista.tabla import mostrar_tabla


def main():
    # Logica
    originales = simular(REGISTROS, PESOS_ORIGINALES)
    ajustados = simular(REGISTROS, PESOS_AJUSTADOS)

    # Vista: tablas
    mostrar_tabla(originales, "MODELO ORIGINAL: I = 0.5H + 0.3N + 0.2Tf")
    mostrar_tabla(ajustados, "MODELO AJUSTADO: I = 0.4H + 0.4N + 0.2Tf")

    # Vista: grafica
    graficas = Graficas()
    graficas.indice_por_hora(originales, ajustados)


if __name__ == "__main__":
    main()
