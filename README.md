# Soluciones-analiticas-y-numericas
Resolución de una EDO Separable: Solución Exacta y Método de Euler

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
