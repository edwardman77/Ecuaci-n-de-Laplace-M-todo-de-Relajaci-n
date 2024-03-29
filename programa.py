#SOLUCIÓN A LA ECUACIÓN DE LAPLACE POR EL MÉTODO DE RELAJACIÓN
#TAREA 3 - ELECTROMAGNETISMO I
#EDWARD ENRIQUE MANOSALVA PINTO - 202115440

#Importación de librerías necesarias.
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import cm

#Función principal para resolver la ecuación de laplace.
def Laplace_Relajacion(N:int,M:int,dx:float,vx0:float,vxa:float,vy0:float,vyb:float):
    """Resuelve la ecuación de Laplace por el método de relajación para una región rectangular en R2, 
    a partir de condiciones de Dirichlet en los cuatro bordes.

    Args:
        N (int): Número de puntos en X
        M (int): Número de puntos en Y
        dx (float): distnacia entre puntos
        vx0 (float): Valor de la función en V(0,y)
        vxa (float): Valor de la función en V(a,y)
        vy0 (float): Valor de la función en V(x,0)
        vyb (float): Valor de la función en V(x,b)

    Returns:
        tuple: Retorna una tupla con 3 elementos, el eje X, el eje Y y la función del potencial resuelta.
    """

    #Crear la cuadricula inicial de la región con los valores iniciales en los cuatro bordes.
    cuadricula = np.random.rand(N,M)*3
    cuadricula[0,:] = vx0
    cuadricula[N-1,:] = vxa
    cuadricula[:,0] = vy0
    cuadricula[:,M-1] = vyb


    #Inicializa la variable diferencia
    diferencia = 1


    #Ejecuta el algoritmo mientras la diferencia entre valores sea mayor a una tolerancia fija de 0.01.
    while diferencia > 0.0000001:

        #Crea una copia de la cuadricula original
        anterior = cuadricula.copy()

        for x in range(1,N-1):
            for y in range(1, M-1):
                #Para cada casilla en el interior de la cuadricula, reemplaza su valor por el promedio de las cuatro casillas circundantes.
                cuadricula[x,y] = (anterior[x-1,y] + anterior[x+1,y] + anterior[x,y+1] + anterior[x,y-1])/4

        #Calcula la diferencia entre iteraciones como el promedio de la diferencia entre la casiila anterior y la nueva. 
        diferencia = np.abs(cuadricula - anterior)
        diferencia = diferencia.mean()


    #Determina los valores de a y b a partir del paso entre puntos y la cantidad de estos.
    a = N*dx
    b = M*dx

    #Crea los ejes x e y.
    x = np.linspace(0,a,N)
    y = np.linspace(0,b,M)

    #Convierte los ejes x e y en una malla para plotear.
    X,Y = np.meshgrid(x,y)

    #Retorna los ejes X e Y además de los valores de la función V sobre el plano.
    return X,Y, cuadricula.T

def graficar_solucion(X:np.matrix, Y:np.matrix, V:np.matrix):
    """Grafica la solución de la ecuación de Laplace como una superficie 3D con gradiente de colores.

    Args:
        X (np.matrix): Eje X 
        Y (np.matrix): Eje Y
        V (np.matrix): Potencial V(x,y)
    """
    #Crea la gráfica de la solución como una proyección en 3D
    fig = plt.figure(dpi=100)
    ax = plt.axes(projection='3d')

    #Plotea la solución a la ecuación de Laplace como una superficie en 3D con un gradiente de colores.
    surf = ax.plot_surface(X, Y, V, cmap=cm.inferno,
                       linewidth=0, antialiased=False)

    #Nombra los ejes de la gráfica y le asigna un título
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Potencial V(x,y)")
    ax.set_title("Solución de la ecuación de Laplace en R2")

    #Crea una barra de colores como referencia.
    fig.colorbar(surf, shrink=0.5, pad=0.2, aspect=5)

    #Muestra la gráfica.
    plt.show()


#Función inicializadora
def iniciar_programa():
    """Función que inicializa el programa y recibe los valores de entrada por parte del usuario para
    la solución de la ecuación de Laplace.
    """

    #Mensaje de entrada
    print("SOLUCIÓN DE LA ECUACIÓN DE LAPLACE EN R2 \n")

    #Solicitud de datos al usuario
    N = int(input("Ingrese el número de puntos en el eje X: "))
    M = int(input("Ingrese el número de puntos en el eje Y: "))

    dx = float(input("Ingrese la distancia entre puntos: "))

    vx0 = float(input("Ingrese el valor de la función en V(0,y): "))
    vxa = float(input("Ingrese el valor de la función en V(a,y): "))

    vy0 = float(input("Ingrese el valor de la función en V(x,0): "))
    vyb = float(input("Ingrese el valor de la función en V(x,b): "))

    #Mensaje de espera
    print("Espere mientras se crea la gráfica de la solución.")

    #Solución de la ecuación de laplace
    X,Y,V = Laplace_Relajacion(N,M,dx,vx0,vxa,vy0,vyb)

    #Gráfica de la solución
    graficar_solucion(X,Y,V)
    

#Llama a la función inicializadora.
if __name__ == "__main__":
    iniciar_programa()


