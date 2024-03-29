#SOLUCIÓN A LA ECUACIÓN DE LAPLACE POR EL MÉTODO DE RELAJACIÓN
#TAREA 3 - ELECTROMAGNETISMO I
#EDWARD ENRIQUE MANOSALVA PINTO - 202115440

#Importación de librerías necesarias.
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import cm

#Importación de las funciones de solución computacional del archivo programa
import programa as lap

#Función para obtener la solución analítica.
def solucion_analitica(N:int,M:int,dx:float,v0:float):
    """A partir de la expresión analítica encontrada en el informe para el ejemplo de testeo, genera una matriz de valores para un área dada,
    con un valor v_0 dado.
    

    Args:
        N (int): Cantidad de puntos en X
        M (int): Cantidad de puntos en Y
        dx (float): distancia entre puntos
        v0 (float): Valor para la constante v_0

    Returns:
        tuple: Retorna una tupla con 3 elementos, el eje X, el eje Y y el potencial según la expresión analítica para 200 valores de n.
    """

    #Determina los valores de a y b a partir del paso entre puntos y la cantidad de estos.
    a = N*dx
    b = M*dx

    #Crea los ejes x e y.
    x = np.linspace(0,a,N)
    y = np.linspace(0,b,M)

    #Convierte los ejes x e y en una malla.
    X,Y = np.meshgrid(x,y)

    #Inicializa el valor del potencial en ceros.
    V = 0

    #Itera la sumatoria de la expresión analítica 200 veces.
    for n in range(1,201):
        #Encuentra los valores de los coeficientes k, C y D, de acuerdo a lo calculado en el informe.
        k = n*np.pi/a
        D = - 2* v0 * (1 - (-1)**n)/(n*np.pi)
        C = -D * (1/np.sinh(k*b)   + np.cosh(k*b)/np.sinh(k*b))

        #Genera la expresión para V haciendo la sumatoria
        V += (np.sin(k*X) * (C*np.sinh(k*Y) + D*np.cosh(k*Y)))
    
    #Retorna los ejes X e Y además de los valores de la función V sobre el plano.
    return X,Y,V

#Función para obtener la solución computacional.
def solucion_computacional(N:int,M:int,dx:float,v0:float):
    """Resuelve la ecuación de Laplace computacionalmente mediante el método de Relajación haciendo uso de 
    la función creada en el archivo programa.

    Args:
        N (int): Cantidad de puntos en X
        M (int): Cantidad de puntos en Y
        dx (float): distancia entre puntos
        v0 (float): Valor para la constante v_0
    Returns:
        tuple: Retorna una tupla con 3 elementos, el eje X, el eje Y y el potencial según el método computacional.
    """
    
    #Llama a la función creada en el archivo programa para resolver computacionalmente el test.
    X,Y,V = lap.Laplace_Relajacion(N,M,dx,0,0,-v0,v0)

    #Retorna los ejes X e Y además de los valores de la función V sobre el plano.
    return X,Y,V

#Función para graficar la solución tanto analítica como computacional del test.
def graficar_comparacion(Xa:np.matrix, Ya:np.matrix, Va:np.matrix, Xc:np.matrix, Yc:np.matrix, Vc:np.matrix):
    """Grafica la solución Analítica y Computacional del ejemplo de testeo en un mismo plot para su comparación.

    Args:
        Xa (np.matrix): Eje X de la solución analítica.
        Ya (np.matrix): Eje Y de la solución analítica.
        Va (np.matrix): Potencial hallado mediante la solución analítica.
        Xc (np.matrix): Eje X de la solución computacional.
        Yc (np.matrix): Eje Y de la solución computacional.
        Vc (np.matrix): Potencial hallado mediante la solución computacional.
    """

    #Crea la gráfica de la solución como una proyección en 3D, con dos subplots.
    fig = plt.figure(dpi=100)
    ax = fig.add_subplot(1,2,1, projection='3d')

    #Plotea la solución analítica como una superficie en 3D con un gradiente de colores.
    surf1 = ax.plot_surface(Xa, Ya, Va, cmap=cm.inferno,
                       linewidth=0, antialiased=False)
    
    #Crea una barra de colores como referencia.
    fig.colorbar(surf1, shrink=0.5, pad=0.2, aspect=5)

    #Asigna un título y unos ejes al primer subplot.
    ax.set_title("Solución Analítica")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Potencial V(x,y)")

    #Crea el segundo subplot para la solución computacional.
    ax2 = fig.add_subplot(1,2,2, projection='3d')

    #Plotea la solución computacional como una superficie en 3D con un gradiente de colores.
    surf2 = ax2.plot_surface(Xc, Yc, Vc, cmap=cm.inferno,
                       linewidth=0, antialiased=False)
    
    #Crea una barra de colores como referencia.
    fig.colorbar(surf2, shrink=0.5, pad=0.2, aspect=5)

    #Asigna un título y unos ejes al segundo subplot.
    ax2.set_title("Solución computacional")
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    ax2.set_zlabel("Potencial V(x,y)")

    #Asigna un título general a toda la figura
    fig.suptitle("Comparación entre soluciones para la Ecuación de Laplace", fontsize=20)

    #Muestra la gráfica.
    plt.show()


#Función para graficar el error absoluto entre las dos soluciones
def graficar_error(X:np.matrix, Y:np.matrix, Va:np.matrix, Vc:np.matrix):
    """Grafica el error absoluto entre las soluciones analítica y computacional como una superficie en 3D con un gradiente de colores.

    Args:
        X (np.matrix): Eje X.
        Y (np.matrix): Eje Y.
        Va (np.matrix): Potencial de la solución analítica.
        Vc (np.matrix): Potencial de la solución computacional.
    """

    #Genera la matriz de error absoluto como la diferencia entre las soluciones.
    error = abs(Va-Vc)

    #Crea la gráfica del error como una proyección en 3D.
    fig = plt.figure(dpi=100)
    ax = plt.axes(projection='3d')

    #Plotea el error como una superficie 3D con un gradiente de colores.
    surf = ax.plot_surface(X, Y, error, cmap=cm.inferno,
                       linewidth=0, antialiased=False)

    #Asigna nombres a los ejes del plot.
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Error")

    #Asigna un título al plot.
    ax.set_title("Error absoluto entre solución computacional y analítica", fontsize=12)

    #Crea una barra de colores como referencia.
    fig.colorbar(surf, shrink=0.5, pad=0.2, aspect=5)

    #Muestra la gráfica
    plt.show()


#Función general del test.
def ejecutar_test():
    """Función que inicializa el test y grafica las soluciones y el error entre ambas.
    """
    #CAMBIAR DE SER NECESARIO:
    #Valores iniciales para el test.
    N = 50
    M = 50
    dx = 0.8
    v0 = 2

    #Mensaje de inicio
    print("EJEMPLO DE TESTEO PARA EL ALGORITMO DE SOLUCIÓN DE LA ECUACIÓN DE LAPLACE EN R2 \n")

    #Mensaje de espera
    print("Espere mientras se crean la gráficas de la soluciones.")

    #Genera las soluciones analitica y computacional
    Xa,Ya,Va = solucion_analitica(N,M,dx,v0)
    Xc,Yc,Vc = solucion_computacional(N,M,dx,v0)

    #Grafica la comparación entre ambas soluciones como un plot con dos subplots.
    graficar_comparacion(Xa,Ya,Va,Xc,Yc,Vc)

    #Grafica el error entre ambas soluciones como una superficie 3D.
    graficar_error(Xa,Ya,Va,Vc)


#Llama a la función inicializadora.
if __name__ == "__main__":
    ejecutar_test()