import re
from sympy import symbols
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, implicit_multiplication_application)

class Utilidades:

    # ============================================================
    # FUNCIÓN PARA PARSEAR Y VOLVER LA FUNCION QUE ENTIENDE SYMPY A UNA FUNCION MATEMATICA ENTENDIDA POR EL USUARIO
    # ============================================================
    def funcion(self, f):
        funcion = str(f)
        funcion = funcion.replace("**", "^").replace("*", "")
        return funcion
    
    # ============================================================
    # FUNCIÓN PARA PARSEAR FUNCIÓN
    # ============================================================
    def obtener_funcion(self):

        while True:
            #borra espacios antes y despues de lo ingresado
            funcion_str = input ("f(x) =").strip().lower()

            #validar que no este vacio
            if funcion_str =="":
                print("Debe de ingresar una funcion")
                continue

            try:
                #la variable x a travez de symbols guarda ahora no un caracter sino un simbolo matematico "crea variables algebraicas simbolicas" para la funcion
                x = symbols("x")

                #Esta funcion permite que el usuario pueda usar el simbolo ^ para potencias, lo cual es mas natural, y luego lo reemplaza por ** que es el formato que Sympy entiende para potencias. Por ejemplo, si el usuario ingresa "x^3 - 2x - 5", esta función lo convierte a "x**3 - 2x - 5" antes de parsear la expresión matemática. Esto hace que la experiencia del usuario sea más intuitiva al ingresar funciones polinomiales.
                funcion_str = funcion_str.replace("^", "**")

                #Linea que permite usar expresiones como 2x**4-3x+4 (asi omite el * entre el coeficinete y la variable)
                #Funcion que ayuda a que numpy pueda utilizar una expresion = 7x este lo pasa al formato entendido por numpy → 7*x
                funcion_str = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", funcion_str)
                
                #Funcion que permite recibir una fucnion 3x ya que esto lo pasa a 3*x entendible por sympy
                transformaciones = (
                    standard_transformations +
                    (implicit_multiplication_application,)
                )

                # Convierte texto a expresión matemática
                f = parse_expr(funcion_str, transformations=transformaciones)
                
                if f.is_Relational:
                    print("\nError: La expresion no es una funcion valida para el metodo de Newton-Raphson mejorado")
                    return None, None
                
                return f, x
                
            except Exception as e:
                print("\nError en la función ingresada.")
                print("Verifique la sintaxis matemática.")
                print(f"Detalle del error: {e}")

                return None, None
            
    #============================================================
    #funcion para validar que ingresen datos a x0 y x1 qu eno sea letras caracteres y qu evaya vacio.
    def leer_float(self, mensaje, valor_por_defecto=None):
        while True:
            dato = input(mensaje).strip()

            # CASO 1: vacío
            if dato == "":
                if valor_por_defecto is not None:
                    return valor_por_defecto
                print("Debe ingresar un valor.")
                continue

            # CASO 2: número inválido
            try:
                return float(dato)
            except ValueError:
                print("Ingrese un número válido, no letras ni caracteres especiales.")