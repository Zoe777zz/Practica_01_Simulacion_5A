"""Capa de vista: datos que pide la guia (H, N, Tf e Indice) en consola."""


def mostrar_tabla(resultados, titulo):
    print()
    print(titulo)
    print("-" * 40)
    print(f"{'Hora':<8}{'H':<8}{'N':<8}{'Tf':<8}{'Indice':<8}")
    print("-" * 40)
    for r in resultados:
        print(f"{r['hora']:<8}{r['H']:<8.2f}{r['N']:<8.2f}{r['Tf']:<8.2f}{r['indice']:<8.4f}")
    print("-" * 40)
