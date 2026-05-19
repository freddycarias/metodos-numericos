from sympy import Rational, symbols, diff
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application
)


class NewtonRaphson:

    def newton_raphson_mejorado(self, f, x0, tolerancia, max_iter):

        # --------------------------------------------------------
        # Declaración de la variable simbólica x
        # --------------------------------------------------------
        x = symbols('x')

        # validación básica
        if isinstance(f, Rational):
            print("\nError: función no válida para Newton")
            return None, [], []
                
        # --------------------------------------------------------
        # Primera derivada f'(x)
        #
        # diff():
        # -------
        # Metodo que calcula derivadas simbólicas automáticamente.
        # --------------------------------------------------------
        f1 = diff(f, x)

        # --------------------------------------------------------
        # Metodo que calcula la segunda derivada f''(x)
        # --------------------------------------------------------
        f2 = diff(f1, x)

        # --------------------------------------------------------
        # Variables de control
        # --------------------------------------------------------
        errores = []
        historial = []

        xn = x0

        # ========================================================
        # BUCLE PRINCIPAL DEL MÉTODO
        # ========================================================
        for i in range(max_iter):

            # --------------------------------------------
            # Evaluación de la función y derivadas
            # --------------------------------------------
            fx = float(f.subs(x, xn))
            f1x = float(f1.subs(x, xn))
            f2x = float(f2.subs(x, xn))

            # --------------------------------------------
            # Denominador del método mejorado
            # --------------------------------------------
            denominador = (f1x ** 2) - (fx * f2x)

            # Validación para evitar división entre cero
            if denominador == 0:
                print("\nError: División entre cero.")
                return None, errores, historial

            # --------------------------------------------
            # Fórmula Newton-Raphson Mejorado
            # --------------------------------------------
            xn1 = xn - ((fx * f1x) / denominador)

            # Evaluamos la función en el nuevo punto xn1
            fx1 = float(f.subs(x, xn1))
            #Metodos que calculasn el error de la funcion.
            #Error relativo
            if xn1 == 0:
                print("\nError: División entre cero.")
                return None, errores, historial

            error_relativo = abs((xn1 - xn) / xn1)
            # Error funcional real
            error_funcional = abs(fx1)
            # Error entre iteraciones
            error_iterativo = abs(xn1 - xn)

            #guardado de las iteraciones y errorres en el historial
            historial.append({
                "iteracion": i + 1,
                "xn": xn,
                "xn1": xn1,
                "fx": fx,
                "error_relativo": error_relativo,
                "error_funcional": error_funcional,
                "error_iterativo": error_iterativo
            })
            # --------------------------------------------
            # Error absoluto
            #
            # abs():
            # ------
            # Devuelve el valor absoluto de un número.
            # --------------------------------------------
            # Error funcional
            """error = abs(fx)

            # Guardamos error
            errores.append(error)"""
            errores.append(error_funcional)
            # --------------------------------------------
            # Verificación de convergencia
            # --------------------------------------------
            #if error < tolerancia:
            if error_funcional < tolerancia and error_iterativo < tolerancia:
                return xn1, errores, historial


            # Actualizamos valor
            xn = xn1

        # Retorna último valor si no converge
        return xn, errores, historial
