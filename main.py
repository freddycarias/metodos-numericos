from GaussSeidel import GaussSeidel


# ==========================================
# INGRESO DE DATOS
# ==========================================

n = int(input("Ingrese el tamaño de la matriz: "))

A = []
b = []

print("\nIngrese los coeficientes de la matriz:")

for i in range(n):

    fila = list(
        map(
            float,
            input(f"Fila {i+1}: ").split()
        )
    )

    A.append(fila)

print("\nIngrese el vector independiente:")

for i in range(n):

    valor = float(
        input(f"b[{i+1}]: ")
    )

    b.append(valor)

# ==========================================
# TOLERANCIA
# ==========================================

tolerancia = float(
    input(
        "\nIngrese la tolerancia "
        "(ejemplo 0.001): "
    )
)

# ==========================================
# CREAR OBJETO
# ==========================================

metodo = GaussSeidel(
    A,
    b,
    tolerancia=tolerancia
)

# ==========================================
# RESOLVER
# ==========================================

solucion = metodo.resolver()

# ==========================================
# RESULTADOS
# ==========================================

print("\n==============================")
print("SOLUCIÓN APROXIMADA")
print("==============================\n")

for i in range(len(solucion)):

    print(f"x{i+1} = {solucion[i]:.6f}")