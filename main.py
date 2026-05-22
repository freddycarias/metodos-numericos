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

from GaussSeidel import GaussSeidel


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

            print(
                "\nPROGRAMA PARA CALCULAR LAS "
                "APROXIMACIONES A LAS RAICES "
                "DE UNA FUNCION POLINOMIAL\n"
                "UTILIZANDO EL METODO DE "
                "NEWTON-RAPHSON MEJORADO."
            )

            print("\n===== MENÚ PRINCIPAL =====")
            print("1. Calcular raíz")
            print("2. Método de Gauss-Seidel")
            print("3. Salir")

            opcion = input("\nSeleccione una opción: ")

            # ====================================================
            # OPCIÓN 1 → NEWTON
            # ====================================================

            if opcion == "1":

                print("\nIngrese la función polinomial")

                print(
                    "Ejemplo:\n"
                    "Forma 1: x**3 - 2*x - 5\n"
                    "Forma 2: x^3-2x-5)"
                )

                # Valida el string
                f, x = self.utilidades.obtener_funcion()

                # Devuelve función en string
                funcion = self.utilidades.funcion(f)

                if f is None:

                    print(
                        "\nFuncion invalida, "
                        "intente nuevamente."
                    )

                    continue

                x0 = self.interfaz.elegir_x0(f, x)

                tolerancia = float(

                    input(

                        "\nLa 'TOLERANCIA' es "
                        "el umbral maximo de "
                        "error a aceptar\n"

                        "Mientras mas pequeño "
                        "el error mas precisa "
                        "la raiz encontrada.\n"

                        "La tolerancia debe "
                        "ser ingresada en "
                        "decimales.\n\n"

                        "Ejemplo 0.001\n"

                        "Ingrese la tolerancia: "
                    )
                )

                max_iter = int(
                    input(
                        "Máximo de iteraciones: "
                    )
                )

                # Ejecutar método
                raiz, errores, historial = (
                    self.newton.newton_raphson_mejorado(
                        f,
                        x0,
                        tolerancia,
                        max_iter
                    )
                )

                if raiz is None:

                    print(
                        "\nSe canceló la "
                        "ejecución del método."
                    )

                    continue

                # Mostrar resultado
                print("\n===== RESULTADO =====")

                print(
                    f"\nRaíz aproximada: {raiz}"
                )

                # ================================================
                # SUBMENÚ
                # ================================================

                while True:

                    print(
                        "\n===== OPCIONES "
                        "DE VISUALIZACIÓN ====="
                    )

                    print("1. Ver errores absolutos")
                    print("2. Ver iteraciones")
                    print("3. Guardar resultados")
                    print("4. Buscar otra raíz")

                    print(
                        "5. Ver aproximación "
                        "a la raíz en gráfica"
                    )

                    print(
                        "6. Regresar al menú principal"
                    )

                    subop = input(
                        "\nSeleccione una opción: "
                    )

                    # --------------------------------------------
                    # ERRORES
                    # --------------------------------------------

                    if subop == "1":

                        self.archivos.mostrar_errores(
                            errores
                        )

                    # --------------------------------------------
                    # ITERACIONES
                    # --------------------------------------------

                    elif subop == "2":

                        self.archivos.mostrar_historial(
                            historial
                        )

                    # --------------------------------------------
                    # GUARDAR
                    # --------------------------------------------

                    elif subop == "3":

                        nombre = input(

                            "\nNombre del archivo "
                            "(ejemplo resultados.txt): "
                        )

                        self.archivos.guardar_resultados(

                            funcion,
                            nombre,
                            raiz,
                            errores,
                            historial
                        )

                    # --------------------------------------------
                    # OTRA RAÍZ
                    # --------------------------------------------

                    elif subop == "4":

                        break

                    # --------------------------------------------
                    # GRÁFICA
                    # --------------------------------------------

                    elif subop == "5":

                        self.graficos.mostrar_iteraciones_grafica(

                            f,
                            x,
                            historial
                        )

                    # --------------------------------------------
                    # REGRESAR
                    # --------------------------------------------

                    elif subop == "6":

                        break

                    else:

                        print("\nOpción inválida.")

            # ====================================================
            # OPCIÓN 2 → GAUSS-SEIDEL
            # ====================================================

            elif opcion == "2":

                volver_menu = False

                while True:

                    print("\n===== MÉTODO DE GAUSS-SEIDEL =====")

                    # ==========================================
                    # DATOS
                    # ==========================================

                    n = int(
                        input(
                            "\nIngrese el tamaño "
                            "de la matriz: "
                        )
                    )

                    A = []
                    b = []

                    print(
                        "\nIngrese los coeficientes "
                        "de la matriz:"
                    )

                    for i in range(n):

                        fila = []

                        print(f"\nFila {i+1}")

                        for j in range(n):

                            valor = float(

                                input(
                                    f"Ingrese A[{i+1}][{j+1}]: "
                                )
                            )

                            fila.append(valor)

                        A.append(fila)

                    print(
                        "\nIngrese el vector independiente:"
                    )

                    for i in range(n):

                        valor = float(
                            input(f"b[{i+1}]: ")
                        )

                        b.append(valor)

                    tolerancia = float(

                        input(
                            "\nIngrese la tolerancia "
                            "(ejemplo 0.001): "
                        )
                    )

                    # ==========================================
                    # MÉTODO
                    # ==========================================

                    metodo = GaussSeidel(

                        A,
                        b,
                        tolerancia=tolerancia
                    )

                    solucion = metodo.resolver()

                    # ==========================================
                    # RESULTADOS
                    # ==========================================

                    print("\n==============================")
                    print("SOLUCIÓN APROXIMADA")
                    print("==============================\n")

                    for i in range(len(solucion)):

                        print(
                            f"x{i+1} = "
                            f"{solucion[i]:.6f}"
                        )

                    # ==========================================
                    # SUBMENÚ
                    # ==========================================

                    while True:

                        print("\n===== OPCIONES =====")

                        print("1. Resolver otro sistema")
                        print("2. Regresar al menú principal")

                        subop = input(
                            "\nSeleccione una opción: "
                        )

                        # --------------------------------------
                        # OTRO SISTEMA
                        # --------------------------------------

                        if subop == "1":

                            break

                        # --------------------------------------
                        # MENÚ PRINCIPAL
                        # --------------------------------------

                        elif subop == "2":

                            volver_menu = True
                            break

                        else:

                            print("\nOpción inválida.")

                    # ==========================================
                    # REGRESAR MENÚ PRINCIPAL
                    # ==========================================

                    if volver_menu:

                        break

            # ====================================================
            # OPCIÓN 3 → SALIR
            # ====================================================

            elif opcion == "3":

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