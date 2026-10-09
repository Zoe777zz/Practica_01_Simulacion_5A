# Práctica 01 - Construcción y simulación computacional de un modelo matemático

| Dato | Detalle |
|---|---|
| Universidad | Universidad Nacional de Loja - FEIRNNR, Carrera de Computación |
| Asignatura | Simulación Ciclo 5 |
| Número de Práctica | 01|
| Unidad | U1: Introducción a la Simulación |
| Docente | José O. Guamán Q. |
| Estudiante | María Soledad Buri Camacho |
| Sistema operativo | Linux  |

## 1. Descripción

El programa simula la atmósfera durante un día y determina en qué horas el modelo considera que existe posibilidad de lluvia. Para esto, utiliza un modelo matemático que calcula un índice de lluvia basado en la humedad (H), nubosidad (N) y un factor de temperatura (Tf).

El sistema evalúa dos escenarios:

Modelo original: I = 0.5H + 0.3N + 0.2Tf.

Modelo ajustado: I = 0.4H + 0.4N + 0.2Tf.
```
I = 0.5·H + 0.3·N + 0.2·Tf
```

- **H**: humedad normalizada (humedad % / 100)
- **N**: nubosidad normalizada (nubosidad % / 100)
- **Tf**: factor de temperatura

Dependiendo del valor del índice calculado, clasifica el estado del clima en: "Sin lluvia", "Baja posibilidad", "Lluvia probable" o "Lluvia".

| Índice I | Estado |
|---|---|
| I < 0.40 | Sin lluvia |
| 0.40 ≤ I < 0.60 | Baja posibilidad |
| 0.60 ≤ I < 0.75 | Lluvia probable |
| I ≥ 0.75 | Lluvia |


## 2. Tecnologías utilizadas

Lenguaje: Python 3.9 o superior.

Librerías: Matplotlib para la generación de gráficas visuales.

Entorno OS: Linux preferentemente.

## 3. Arquitectura (por capas)

```

practica01_simulacion/
├── main.py                     # Punto de entrada: conecta las capas
├── requirements.txt            # Dependencias
├── README.md
├── .gitignore
├── datos/
│   └── datos_clima.py          # CAPA DE DATOS: registros, umbrales, pesos
├── logica/
│   └── modelo_lluvia.py        # CAPA DE LÓGICA: funciones del factor Tf, índice y estado
└── vista/
    ├── tabla.py                # CAPA DE VISTA: tabla en consola (H, N, Tf, Índice)
    └── graficas.py             # CAPA DE VISTA: gráfica con Matplotlib
```


## 3. Requisitos previos

Esta práctica se ejecuta en **Linux**. Se necesitan estos paquetes del sistema:

- `python3` (3.9 o superior)
- `python3-venv` (para crear el entorno virtual)
- `python3-pip`
- `python3-tk` (para que se abra la ventana de la gráfica)
- `git` (para clonar el repositorio)

Instalarlos :

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip python3-tk git
```

Verificar la versión de Python:

```bash
python3 --version
```

Debe mostrar `Python 3.9` o superior.

## 4. Instalación y ejecución (paso a paso)

Todos los comandos se ejecutan en una terminal de Linux.

### Paso 1. Obtener el proyecto

```bash
git clone <URL-DEL-REPOSITORIO>
cd practica01_simulacion
```

(Reemplazar `<URL-DEL-REPOSITORIO>` por la dirección del repositorio. Si se descargó un ZIP, descomprimirlo con `unzip practica01_simulacion.zip` y entrar con `cd practica01_simulacion`.)

A partir de aquí **todos los comandos se ejecutan dentro de la carpeta `practica01_simulacion`**, donde están `main.py` y `requirements.txt`. Para comprobarlo:

```bash
ls
```

Debe mostrar: `datos  logica  main.py  README.md  requirements.txt  vista`

### Paso 2. Crear el entorno virtual

```bash
python3 -m venv venv
```

Esto crea una carpeta llamada `venv`.

### Paso 3. Activar el entorno virtual

```bash
source venv/bin/activate
```

Cuando está activo, la terminal muestra `(venv)` al inicio de la línea.

### Paso 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

Esto instala NumPy y Matplotlib. Debe terminar con un mensaje como `Successfully installed ...`.

### Paso 5. Ejecutar el programa

```bash
python main.py
```

### Paso 6. Qué se espera ver

1. En la terminal se imprimen **dos tablas** (modelo original y modelo ajustado) con las columnas Hora, H, N, Tf e Índice.
2. Se abre **una ventana con una sola gráfica**: el índice de lluvia por hora de los dos modelos, con líneas punteadas en los límites 0.40, 0.60 y 0.75.
3. Para terminar el programa, cerrar la ventana de la gráfica.

### Paso 7. Desactivar el entorno virtual (opcional)

```bash
deactivate
```

## 5. Resultados del modelo original (verificación)

| Hora | H | N | Tf | Índice |
|---|---|---|---|---|
| 06:00 | 0.65 | 0.40 | 0.80 | 0.6050 |
| 08:00 | 0.70 | 0.50 | 0.70 | 0.6400 |
| 10:00 | 0.68 | 0.45 | 0.60 | 0.5950 |
| 12:00 | 0.60 | 0.30 | 0.40 | 0.4700 |
| 14:00 | 0.75 | 0.70 | 0.50 | 0.6850 |
| 16:00 | 0.85 | 0.85 | 0.60 | 0.8000 |
| 18:00 | 0.92 | 0.95 | 0.70 | 0.8850 |
| 20:00 | 0.88 | 0.90 | 0.65 | 0.8400 |
| 22:00 | 0.80 | 0.75 | 0.75 | 0.7750 |

