from utilidades import Utilidades
from graficos import Graficador
from sympy import sympify
from sympy.core.sympify import SympifyError
import numpy as np

class Interfaz:

    def __init__(self):
        self.graficos = Graficador()
        self.utilidades = Utilidades()

# ============================================================
# FUNCIÓN PARA ELEGIR x0
# ============================================================

    def elegir_x0(self, f, x):

        opcion = input("\n¿Desea usar la gráfica para elegir el intervalo donde la funcion cambia de signo (corta el eje X)? (s/n): ").lower()

        if opcion == "s":

            self.graficos.graficar_funcion(f, x)
            
            x0 = self.utilidades.leer_float("Ingrese X0: ")
            x1 = self.utilidades.leer_float("Ingrese X1: ")
        
            fx0 = float(f.subs(x, x0))
            fx1 = float(f.subs(x, x1))

            # Validación de raíz en intervalo
            if fx0 * fx1 > 0:
                print("\nNo hay cambio de signo. El intervalo puede no contener raíz.")
                return (x0 + x1) / 2

            xr = (x0 + x1) / 2
            self.graficos.graficar_funcion(f, x, xr)

            print(f"\nValor inicial recomendado (punto medio): {xr}")
            return xr

        else:

            print("\nOpciones:")
            print("1. Valor manual")
            print("2. Valor aleatorio")

            op = input("Seleccione: ")

            if op == "1":
                return float(input("Ingrese X0: "))

            elif op == "2":
                return np.random.uniform(-5, 5)

            else:
                print("Opción inválida, usando X0 = 1")
                return 1