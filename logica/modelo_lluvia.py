


def factor_temperatura(temp):

    tf = 1.0 - ((temp - 10) / 2) * 0.1
    tf = min(1.0, max(0.1, tf))
    return round(tf, 2)


def calcular_indice(h, n, tf, pesos):
    peso_h, peso_n, peso_tf = pesos
    indice = peso_h * h + peso_n * n + peso_tf * tf
    return round(indice, 4)


def clasificar(indice):
    if indice < 0.40:
        return "Sin lluvia"
    elif indice < 0.60:
        return "Baja posibilidad"
    elif indice < 0.75:
        return "Lluvia probable"
    else:
        return "Lluvia"


def simular(registros, pesos):
    resultados = []
    for hora, humedad, nubosidad, temp in registros:
        h = humedad / 100
        n = nubosidad / 100
        tf = factor_temperatura(temp)
        indice = calcular_indice(h, n, tf, pesos)
        resultados.append({
            "hora": hora,
            "humedad": humedad,
            "nubosidad": nubosidad,
            "temp": temp,
            "H": h,
            "N": n,
            "Tf": tf,
            "indice": indice,
            "estado": clasificar(indice),
        })
    return resultados
