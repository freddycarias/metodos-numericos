# MÉTODO DE NEWTON-RAPHSON MEJORADO PARA FUNCIONES POLINOMIALES

# ============================================================
# DESCRIPCIÓN:
# Este programa permite:
# 1. Encontrar raíces de funciones polinomiales.
#       -Graficar la funcion
# 2. Usar el método de Newton-Raphson Mejorado.
# 3. Mostrar:
#       - Error relativo
#       - Iteraciones
#       - Error absoluto (funcionales)
#       - Aproximaciones sucesivas
# 4. Guardar resultados en un archivo TXT.
# 5. Resolver múltiples funciones desde un menú.
# 6. Graficar la funcion con los resultados de las iteraciones

# ============================================================
# LIBRERÍAS UTILIZADAS:
# sympy:
# Librería matemática simbólica.
# Permite:
#   - Derivar funciones automáticamente
#   - Evaluar expresiones matemáticas
#   - Manejar variables simbólicas
#
# math:
# Librería matemática estándar de Python.
# Se usa para:
#   - valores absolutos
#   - operaciones numéricas
#
#matplotlib:
#Libreria para graficar funciones y mostrar iteraciones en graficas.
#
#numpy:
#LIbreria para manejar arreglos numericos y generar valores para graficar funciones.

# ============================================================
# FUNCIÓN: newton_raphson_mejorado
# Esta función implementa el método de Newton-Raphson Mejorado.
# Fórmula utilizada:
#
#              f(x) * f'(x)
# Xn+1 = Xn - -------------------------
#          [f'(x)]² - f(x)*f''(x)
#
# Ventajas:
# - Mayor estabilidad
# - Mejor convergencia
# - Reduce problemas cuando f'(x) ≈ 0

# PARÁMETROS:
# funcion_str : función ingresada como texto
# x0          : valor inicial
# tolerancia  : error permitido
# max_iter    : número máximo de iteraciones
#
# RETORNA:1
# raiz                -> raíz aproximada
# errores             -> lista de errores absolutos
# historial           -> lista de iteraciones


from archivos import Archivos
from graficos import Graficador
from interfaz import Interfaz
from newton import NewtonRaphson
from utilidades import Utilidades

class Main1:

    def __init__(self):
        self.archivos = Archivos()
        self.graficos = Graficador()
        self.interfaz = Interfaz()
        self.newton = NewtonRaphson()
        self.utilidades = Utilidades()

    # ============================================================
    # MENÚ PRINCIPAL
    # ============================================================

    def menu(self):

        while True:
            print("\nPROGRAMA PARA CALCULAR LAS APROXIMACIONES A LAS RAICES DE UNA FUNCION POLINOMIAL\n" \
            "UTILIZANDO EL METODO DE NEWTON-RAPHSON MEJORADO.")
            print("\n===== NEWTON-RAPHSON MEJORADO =====")
            print("1. Calcular raíz")
            print("2. Salir")

            opcion = input("\nSeleccione una opción: ")

            # ====================================================
            # OPCIÓN 1
            # ====================================================
            if opcion == "1":
                print("\nIngrese la función polinomial")
                print("Ejemplo:\nForma 1: x**3 - 2*x - 5\n"
                "Forma 2: x^3-2x-5)"
                )
                
                #Valida el string y lo convierte en una expresion matematica para ser evaluada
                f, x = self.utilidades.obtener_funcion()

                # develeve la expresion matematica en string
                funcion = self.utilidades.funcion(f)

                if f is None:
                    print("\nFuncion invalida, intente nuevamente.")
                    continue

                x0 = self.interfaz.elegir_x0(f, x)
                
                tolerancia = float(input("\nLa 'TOLERANCIA' es el umbral maximo de error a aceptar\n"
                "Mientras mas pequeño el error mas precisa la raiz encontrada.\n" \
                "La tolerancia debe ser ingresada en decimales.\n\nTolerancia en DECIMALES\nEjemplo 0.001\nIngrese la tolerancia: "))
                max_iter = int(input("Máximo de iteraciones: "))

                # Ejecutamos método
                raiz, errores, historial = self.newton.newton_raphson_mejorado(
                    f,
                    x0,
                    tolerancia,
                    max_iter
                    )
                
                if raiz is None:
                    print("\nSe cancelo la ejecucion del método.\nRegresando al menú...")
                    continue
                
                
                # Mostrar raíz
                print("\n===== RESULTADO =====")
                print(f"\nRaíz aproximada: {raiz}")

                # ================================================
                # SUBMENÚ DE VISUALIZACIÓN
                # ================================================
                while True:

                    print("\n===== OPCIONES DE VISUALIZACIÓN =====")
                    print("1. Ver errores absolutos")
                    print("2. Ver iteraciones")
                    print("3. Guardar resultados")
                    print("4. Buscar otra raíz")
                    print("5. Ver la aproximación a la RAIZ de las iteraciones en gráfica")
                    print("6. Regresar al menú principal")
                    

                    subop = input("\nSeleccione una opción: ")

                    # --------------------------------------------
                    # Mostrar errores
                    # --------------------------------------------
                    if subop == "1":
                        self.archivos.mostrar_errores(errores)

                    # --------------------------------------------
                    # Mostrar historial
                    # --------------------------------------------
                    elif subop == "2":
                        self.archivos.mostrar_historial(historial)

                    # --------------------------------------------
                    # Guardar archivo
                    # --------------------------------------------
                    elif subop == "3":
                        nombre = input(
                            "\nNombre del archivo (ejemplo resultados.txt): "
                        )

                        self.archivos.guardar_resultados(
                            funcion,
                            nombre,
                            raiz,
                            errores,
                            historial
                        )

                    # --------------------------------------------
                    # Buscar otra raíz
                    # --------------------------------------------
                    elif subop == "4":
                        break
                    
                    
                    # --------------------------------------------
                    # GRAFICAR CON LAS
                    # --------------------------------------------
                    elif subop == "5":
                        self.graficos.mostrar_iteraciones_grafica(f, x, historial)

                    # --------------------------------------------
                    # Regresar menú principal
                    # --------------------------------------------
                    elif subop == "6":
                        break

                    else:
                        print("\nOpción inválida.")

            # ====================================================
            # OPCIÓN 2
            # ====================================================
            elif opcion == "2":

                print("\nPROGRAMA FINALIZADO...")
                break

            else:
                print("\nOpción inválida.")


    # ============================================================
    # INICIO DEL PROGRAMA
    # ============================================================


if __name__ == "__main__":
    programa = Main1()
    programa.menu()


"""import os

print(os.getcwd()) "para verificar el directorio actual, util para saber donde se guardan los archivos de los resultados."""