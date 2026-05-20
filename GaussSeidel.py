import numpy as np


class GaussSeidel:

    def __init__(

        self,
        A,
        b,
        tolerancia=1e-3,
        max_iter=100

    ):

        self.A = np.array(
            A,
            dtype=float
        )

        self.b = np.array(
            b,
            dtype=float
        )

        self.tolerancia = tolerancia
        self.max_iter = max_iter

        self.n = len(A)

    # ==========================================
    # REORDENAR MATRIZ
    # ==========================================

    def reordenar_matriz(self):

        usado = [False] * self.n

        nueva_A = np.zeros_like(
            self.A,
            dtype=float
        )

        nueva_b = np.zeros_like(
            self.b,
            dtype=float
        )

        for col in range(self.n):

            mayor = -1
            fila_mayor = -1

            for fila in range(self.n):

                if not usado[fila]:

                    if abs(self.A[fila][col]) > mayor:

                        mayor = abs(
                            self.A[fila][col]
                        )

                        fila_mayor = fila

            usado[fila_mayor] = True

            nueva_A[col] = self.A[fila_mayor]
            nueva_b[col] = self.b[fila_mayor]

        self.A = nueva_A
        self.b = nueva_b

    # ==========================================
    # VALIDAR DIAGONAL DOMINANTE
    # ==========================================

    def es_diagonal_dominante(self):

        for i in range(self.n):

            diagonal = abs(
                self.A[i][i]
            )

            suma = 0

            for j in range(self.n):

                if i != j:

                    suma += abs(
                        self.A[i][j]
                    )

            if diagonal < suma:

                return False

        return True

    # ==========================================
    # MÉTODO GAUSS-SEIDEL
    # ==========================================

    def resolver(self):

        # Vector inicial
        x = np.zeros(self.n)

        # Lista de errores
        errores = []

        print("\n==============================")
        print("MATRIZ ORIGINAL")
        print("==============================\n")

        print(self.A)

        # ======================================
        # REORDENAR MATRIZ
        # ======================================

        self.reordenar_matriz()

        print("\n==============================")
        print("MATRIZ REORDENADA")
        print("==============================\n")

        print(self.A)

        print("\n==============================")
        print("VECTOR INDEPENDIENTE")
        print("==============================\n")

        print(self.b)

        # ======================================
        # VALIDAR DIAGONAL DOMINANTE
        # ======================================

        print("\n==============================")
        print("VALIDACIÓN")
        print("==============================")

        if self.es_diagonal_dominante():

            print(
                "\nLa matriz ES "
                "diagonal dominante."
            )

        else:

            print(
                "\nAdvertencia:"
            )

            print(
                "La matriz NO es "
                "diagonal dominante."
            )

            print(
                "El método podría "
                "no converger."
            )

        # ======================================
        # ITERACIONES
        # ======================================

        print("\n==============================")
        print("ITERACIONES")
        print("==============================")

        for k in range(self.max_iter):

            x_old = x.copy()

            print(f"\nIteración {k+1}")

            for i in range(self.n):

                suma1 = 0
                suma2 = 0

                # --------------------------------
                # Valores nuevos
                # --------------------------------

                for j in range(i):

                    suma1 += (
                        self.A[i][j] * x[j]
                    )

                # --------------------------------
                # Valores anteriores
                # --------------------------------

                for j in range(
                    i + 1,
                    self.n
                ):

                    suma2 += (
                        self.A[i][j]
                        * x_old[j]
                    )

                # --------------------------------
                # Fórmula Gauss-Seidel
                # --------------------------------

                x[i] = (

                    self.b[i]
                    - suma1
                    - suma2

                ) / self.A[i][i]

            # ==================================
            # MOSTRAR VECTOR ACTUAL
            # ==================================

            print(

                " | ".join(

                    [

                        f"x{i+1}={x[i]:.6f}"

                        for i in range(self.n)

                    ]
                )
            )

            # ==================================
            # ERROR
            # ==================================

            error = np.linalg.norm(

                x - x_old,

                ord=np.inf
            )

            errores.append(error)

            print(
                f"Error = {error:.10f}"
            )

            # ==================================
            # CONVERGENCIA
            # ==================================

            if error < self.tolerancia:

                print("\n==============================")
                print("CONVERGENCIA ALCANZADA")
                print("==============================")

                print(
                    f"\nIteraciones realizadas: "
                    f"{k+1}"
                )

                print(
                    f"Error final: "
                    f"{error:.10f}"
                )

                print(
                    "\nNorma utilizada:"
                )

                print("Norma infinito")

                print(
                    "\nLa solución converge "
                    "porque el error es "
                    "menor que la tolerancia."
                )

                return x

        # ======================================
        # NO CONVERGIÓ
        # ======================================

        print("\n==============================")
        print("NO CONVERGIÓ")
        print("==============================")

        print(
            f"\nSe alcanzó el máximo "
            f"de iteraciones "
            f"({self.max_iter})."
        )

        return x