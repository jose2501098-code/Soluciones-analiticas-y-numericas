"""
Resolución analítica y numérica (Método de Euler) de una EDO separable.

Ecuación diferencial seleccionada:
    dy/dt = 2 * t * y,   con condición inicial y(0) = 1

Solución exacta (por separación de variables):
    y(t) = exp(t^2)

Intervalo de evaluación: t en [0, 1]
Tamaño de paso: h = 0.2
"""

from __future__ import annotations

import math
from typing import Callable, List, Tuple


def f(t: float, y: float) -> float:
    """Evalúa el lado derecho de la EDO separable dy/dt = 2 * t * y."""
    return 2.0 * t * y


def solucion_exacta(t: float) -> float:
    """Devuelve el valor exacto y(t) = exp(t^2) obtenido por separación de variables."""
    return math.exp(t**2)


def metodo_euler(
    funcion_pendiente: Callable[[float, float], float],
    t0: float,
    y0: float,
    t_fin: float,
    h: float,
) -> List[Tuple[int, float, float, float, float, float]]:
    """
    Aproxima la solución de dy/dt = f(t, y) mediante el método de Euler.

    Retorna una lista de tuplas con:
        (n, t_n, y_euler, y_exacta, error_absoluto, error_relativo_pct)
    """
    n_pasos = round((t_fin - t0) / h)
    resultados: List[Tuple[int, float, float, float, float, float]] = []

    t = t0
    y = y0

    for n in range(n_pasos + 1):
        y_ex = solucion_exacta(t)
        err_abs = abs(y_ex - y)
        err_rel_pct = (err_abs / abs(y_ex)) * 100.0 if y_ex != 0 else 0.0
        resultados.append((n, t, y, y_ex, err_abs, err_rel_pct))

        if n < n_pasos:
            y = y + h * funcion_pendiente(t, y)
            t = round(t0 + (n + 1) * h, 10)

    return resultados


def imprimir_resultados(
    resultados: List[Tuple[int, float, float, float, float, float]],
) -> None:
    """Imprime en consola el resumen del problema y la tabla comparativa."""
    print("Ecuación diferencial separable: dy/dt = 2*t*y,  y(0) = 1")
    print("Solución exacta (separación de variables): y(t) = e^(t^2)")
    print("Método numérico: Euler explícito en t ∈ [0, 1] con paso h = 0.2\n")

    encabezado = (
        f"{'n':>2} | {'t_n':>5} | {'y_Euler':>12} | {'y_Exacta':>12} | "
        f"{'Error Abs.':>12} | {'Error Rel. (%)':>14}"
    )
    separador = "-" * len(encabezado)
    print(encabezado)
    print(separador)

    for n, t, y_eul, y_ex, err_abs, err_rel in resultados:
        print(
            f"{n:>2} | {t:>5.1f} | {y_eul:>12.6f} | {y_ex:>12.6f} | "
            f"{err_abs:>12.6f} | {err_rel:>13.2f}%"
        )


def graficar_comparacion(
    resultados: List[Tuple[int, float, float, float, float, float]],
    ruta_imagen: str = "comparacion_euler.png",
) -> None:
    """Genera una gráfica comparando la solución exacta con la aproximación de Euler."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print(
            "\nNota: 'matplotlib' no está instalado; se omitió la generación de la gráfica."
        )
        return

    t_euler = [fila[1] for fila in resultados]
    y_euler = [fila[2] for fila in resultados]

    # Curva suave para la solución exacta
    n_curva = 200
    t_curva = [i / n_curva for i in range(n_curva + 1)]
    y_curva = [solucion_exacta(t) for t in t_curva]

    plt.figure(figsize=(8, 5))
    plt.plot(
        t_curva,
        y_curva,
        label=r"Solución exacta: $y(t) = e^{t^2}$",
        color="#1f77b4",
        linewidth=2.2,
    )
    plt.plot(
        t_euler,
        y_euler,
        "o--",
        label="Método de Euler ($h = 0.2$)",
        color="#d62728",
        linewidth=1.8,
        markersize=7,
    )

    plt.title(r"Comparación: Solución Exacta vs. Método de Euler ($dy/dt = 2ty$, $y(0)=1$)")
    plt.xlabel("$t$")
    plt.ylabel("$y(t)$")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig(ruta_imagen, dpi=150)
    plt.close()
    print(f"\nGráfica guardada en: {ruta_imagen}")


def main() -> None:
    t0 = 0.0
    y0 = 1.0
    t_fin = 1.0
    h = 0.2

    resultados = metodo_euler(f, t0, y0, t_fin, h)
    imprimir_resultados(resultados)
    graficar_comparacion(resultados)


if __name__ == "__main__":
    main()Resolución de una EDO Separable: Solución Exacta y Método de Euler

Este repositorio presenta la resolución analítica (mediante el método de separación de variables) y la aproximación numérica (mediante el método de Euler explícito) de una ecuación diferencial ordinaria (EDO) separable en Python.

1. Planteamiento del problema

Se selecciona el siguiente problema de valor inicial (PVI):

$$\frac{dy}{dt} = 2ty, \qquad y(0) = 1$$

El objetivo es:

Obtener la solución exacta $y(t)$ de forma analítica usando separación de variables.

Aproximar la solución en el intervalo $t \in [0, 1]$ usando el método de Euler con tamaño de paso $h = 0.2$.

Comparar ambas soluciones y cuantificar el error absoluto y relativo en cada nodo.

2. Solución analítica (separación de variables)

Partiendo de:

$$\frac{dy}{dt} = 2ty$$

Separar variables (para $y \neq 0$):


$$\frac{1}{y}\,dy = 2t\,dt$$

Integrar ambos lados:


$$\int \frac{1}{y}\,dy = \int 2t\,dt$$

$$\ln\vert{}y\vert{} = t^2 + C$$

Despejar $y(t)$:


$$y(t) = K e^{t^2}, \qquad K = \pm e^C$$

Aplicar la condición inicial $y(0) = 1$:


$$1 = K e^{0^2} \implies K = 1$$

Por lo tanto, la solución exacta del PVI es:

$$y(t) = e^{t^2}$$

3. Aproximación numérica (método de Euler)

El método de Euler explícito aproxima la solución de $\frac{dy}{dt} = f(t, y)$ mediante la recurrencia:

$$t_{n+1} = t_n + h, \qquad y_{n+1} = y_n + h \cdot f(t_n, y_n)$$

Con $f(t, y) = 2ty$, $t_0 = 0$, $y_0 = 1$ y $h = 0.2$ sobre $[0, 1]$ ($N = 5$ pasos):

Paso 0 ($t_0 = 0.0$): $y_0 = 1.000000$

Paso 1 ($t_1 = 0.2$): $y_1 = 1 + 0.2 \cdot (2 \cdot 0.0 \cdot 1) = 1.000000$

Paso 2 ($t_2 = 0.4$): $y_2 = 1 + 0.2 \cdot (2 \cdot 0.2 \cdot 1) = 1.080000$

Paso 3 ($t_3 = 0.6$): $y_3 = 1.08 + 0.2 \cdot (2 \cdot 0.4 \cdot 1.08) = 1.252800$

Paso 4 ($t_4 = 0.8$): $y_4 = 1.2528 + 0.2 \cdot (2 \cdot 0.6 \cdot 1.2528) = 1.553472$

Paso 5 ($t_5 = 1.0$): $y_5 = 1.553472 + 0.2 \cdot (2 \cdot 0.8 \cdot 1.553472) = 2.050583$

4. Comparación de resultados

Paso ($n$)

$t_n$

$y_{\text{Euler}}$

$y_{\text{Exacta}} = e^{t_n^2}$

Error absoluto

Error relativo (%)

0

0.0

1.000000

1.000000

0.000000

0.00%

1

0.2

1.000000

1.040811

0.040811

3.92%

2

0.4

1.080000

1.173511

0.093511

7.97%

3

0.6

1.252800

1.433329

0.180529

12.60%

4

0.8

1.553472

1.896481

0.343009

18.09%

5

1.0

2.050583

2.718282

0.667699

24.56%

Análisis breve del error

Como la segunda derivada $y''(t) = (2 + 4t^2)e^{t^2}$ es estrictamente positiva en $[0, 1]$, la curva exacta es convexa (cóncava hacia arriba). Dado que el método de Euler avanza usando la pendiente tangente al inicio de cada subintervalo, las aproximaciones quedan siempre por debajo de la curva exacta y el error acumulado crece conforme aumenta $t$. Reducir el tamaño de paso $h$ disminuye este error de forma proporcional a $h$ (orden global $O(h)$).

5. Estructura del repositorio

euler_edo_separable.py: script principal que evalúa la solución exacta, ejecuta el método de Euler, imprime la tabla comparativa y genera una gráfica comparativa (comparacion_euler.png).

README.md: documentación del problema, derivación matemática, resultados e instrucciones de uso.

6. Ejecución

El cálculo numérico utiliza únicamente la biblioteca estándar de Python (math). Para generar además la gráfica comparativa, se requiere matplotlib (opcional).

python3 euler_edo_separable.py


Si deseas habilitar la gráfica y no tienes matplotlib instalado:

pip install matplotlib
