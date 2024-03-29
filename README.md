# ECUACIÓN DE LAPLACE - MÉTODO DE RELAJACIÓN

En este repositorio se encuentra el desarrollo computacional de un algoritmo implementado en Python para resolver la ecuación de Laplace en una región rectangular bidimensional mediante el método de Relajación, como parte de la solución a la *Tarea #3* del curso **ELECTROMAGNETISMO I**.

*Edward Enrique Manosalva Pinto - 202115440*

Se encuentran dos archivos `.py`:

## Programa.py

En este archivo se encuentra el desarrollo general del algoritmo. Cuenta con una interfaz diseñada para su uso por parte de un usuario cualquiera, sencillamente ejecútelo y rellene los campos que se le piden en consola. Posteriormente deberá aparecer la gráfica de la solución con las condiciones ingresadas. **No es necesario modificar el código fuente para su uso.**

*Advertencia:* La generación de la gráfica podría tardar un poco, si es el caso, por favor tenga paciencia.

## Test.py

En este archivo se encuentra la solución al ejemplo de testeo propuesto en la guía. Genera una gráfica comparativa entre la solución analítica al ejemplo y la solución mediante el algoritmo computacional, así como una grafica del error absoluto entre estas dos.

Este archivo es autocontenido, lo que significa que con solo ejecutarlo es suficiente para su funcionamiento. Sin embargo, es necesario que esté en la misma carpeta que el archivo programa.py, puesto que usa funciones creadas en este.

Por defecto, este archivo contiene los siguientes parámetros para el ejemplo:

| Parámetro |Valor  |
|--|--|
| N | 50 |
|M|50|
|dx|0.8|
|$v_0$|2|

Si desea cambiar alguno de estos, en la línea `151` encontrará las variables de cada parámetro, donde podrá realizar el cambio, sin embargo, con los valores que trae por defecto funciona bastante bien.
