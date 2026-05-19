import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols

class Graficador:

    # ============================================================
    #funcion para graficar la funcion.
    def graficar_funcion(self, f, x, xr=None):

        x_vals = np.linspace(-20, 20, 100)
        y_vals = []

        for val in x_vals:
            try:
                y_vals.append(float(f.subs(x, val)))
            except:
                y_vals.append(np.nan)

        plt.figure(figsize=(10, 5))

        plt.plot(x_vals, y_vals, label="f(x)")

        # Mostrar posible raíz
        if xr is not None:
            plt.scatter(
                xr,
                0,
                color="red",
                s=100,
                label="Posible raíz"
            )

        plt.axhline(0, color="black")
        plt.axvline(0, color="black")

        plt.ylim(-20, 20)
        plt.xlim(-20, 20)

        plt.xticks(np.arange(-20, 21, 1))
        plt.yticks(np.arange(-20, 21, 1))

        plt.grid()
        plt.legend()

        plt.title("Gráfica de la función\nCIERRE LA VENTANA PARA CONTINUAR")
        plt.xlabel("x")
        plt.ylabel("f(x)")

        plt.show()


    # ============================================================
    #funcioin para graficar la funcion y la aproximacion de la raiz en cada iteracion.
    def mostrar_iteraciones_grafica(self, f, x, historial):

        # Valores para la curva
        x_vals = np.linspace(-20, 20, 400)

        y_vals = []

        for val in x_vals:
            try:
                y_vals.append(float(f.subs(x, val)))
            except:
                y_vals.append(np.nan)

        # Crear ventana
        plt.figure(figsize=(12, 6))

        # Función
        plt.plot(x_vals, y_vals, label="f(x)", color="blue")

        # Ejes
        plt.axhline(0, color="black")
        plt.axvline(0, color="black")

        # Dibujar aproximaciones
        for dato in historial:

            xn1 = dato["xn1"]

            try:
                fxn1 = float(f.subs(x, xn1))

                plt.scatter(
                    xn1,
                    fxn1,
                    color="red",
                    s=80
                )

                # Texto de iteración
                plt.text(
                    xn1,
                    fxn1,
                    f"I{dato['iteracion']}",
                    fontsize=8
                )

            except:
                pass

        plt.xlim(-20, 20)
        plt.ylim(-20, 20)

        plt.grid()

        plt.legend()

        plt.title("Aproximaciones de Newton-Raphson Mejorado\nCIERRE LA VENTANA PARA CONTINUAR")

        plt.xlabel("x")
        plt.ylabel("f(x)")

        plt.show()
