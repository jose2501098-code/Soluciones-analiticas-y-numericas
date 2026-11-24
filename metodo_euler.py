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
    main()