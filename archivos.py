from sympy import symbols
class Archivos:

    # ============================================================
    # FUNCIÓN: mostrar_errores
    # ============================================================
    #
    # Muestra únicamente los errores absolutos.
    #
    # ============================================================
    #mostraba errores absolutos, pero ahora se muestra la evolución del error en cada iteración, para que el usuario pueda ver cómo va disminuyendo el error a medida que se acerca a la raíz.

    """def mostrar_errores(errores):

        print("\n===================================")
        print(" ERRORES ABSOLUTOS")
        print("===================================")

        for i, e in enumerate(errores):
            print(f"Iteración {i+1}: {e}")"""

    def mostrar_errores(self, errores):

        print("\n===== ERROR ABSOLUTO =====")

        for i, error in enumerate(errores):

            print(f"Iteración {i+1} --> Error = {error}")

    # ============================================================
    # FUNCIÓN: mostrar_historial
    # ============================================================
    # Muestra:
    #   - Iteraciones
    #   - Valores aproximados
    #   - Error absoluto
    # ============================================================

    def mostrar_historial(self, historial):

        print("\n===== HISTORIAL DE ITERACIONES =====")

        for dato in historial:

            print(f"\nIteración: {dato['iteracion']}")
            print(f"Xn     = {dato['xn']}")
            print(f"Xn+1   = {dato['xn1']}")
            print(f"f(Xn)   = {dato['fx']}")
            print(f"Error relativo = {dato['error_relativo']:.6%}","Nos indica en porcentaje que tan grande es el cambio respecto al valor actual\n" \
            "Cambio grande lejos de la raiz\nCambio pequeño cerca de la raiz")
            print(f"Error funcional = {dato['error_funcional']}","Nos indica cuanto cambio la funcion respecto a 0, el valor que satisface la ecuacion\n" \
            "Valor grande lejos de la raiz\nvalor pequeño cerca de la raiz")
            print(f"Error absoluto (iterativo) = {dato['error_iterativo']}","Nos indica cuanto cambio el valor de Xn respecto a la iteracion anterior\n" \
            "Valor grande lejos de la raiz\nValor pequeño cerca de la raiz")
            print(f"APROXIMACION A LA RAIZ DE LA FUNCION EN EL INTERVALO SELECCIONADO, EN ESTA ITERACION: {dato['xn1']}")

    # ============================================================
    # FUNCIÓN: guardar_resultados
    # ============================================================
    #
    # Guarda resultados en un archivo TXT.
    #
    # open():
    # -------
    # Permite abrir archivos.
    #
    # "w":
    # ----
    # Modo escritura.
    #
    # ============================================================
    def guardar_resultados(self, f, nombre_archivo, raiz, errores, historial):
        
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:

            archivo.write("\n=====RESULTADOS DEL METODO NEWTON-RAPHSON MEJORADO=====\n\n")
            archivo.write(f"Datos de la funcion: f(x) = {f}\n\n")
            archivo.write(f"Raíz aproximada: {raiz}\n\n")

            archivo.write("ERRORES ABSOLUTOS:\n")
            for i, e in enumerate(errores):
                archivo.write(f"Iteración {i+1}: {e}\n")

            archivo.write("\nHISTORIAL DE ITERACIONES:\n")

            for dato in historial:
                archivo.write(
                    f"Iteración {dato['iteracion']} -> "
                    f"Xn = {dato['xn']} | "
                    f"Xn+1 = {dato['xn1']} | "
                    f"Error relativo = {dato['error_relativo']} |"
                    f"Error funcional = {dato['error_funcional']} | Error iterativo = {dato['error_iterativo']}\n"
                )

        print("\nResultados guardados correctamente!!!")