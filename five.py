from datetime import datetime


def sumarNumeros(num1, num2):
    return int(num1 + num2)
        
def restarNumeros(num1, num2):
    return int(num1 - num2)

def multiplicarNumeros(num1, num2):
    return int(num1 * num2)

def dividirNumeros(num1, num2):
    if num2 == 0:
        return "Error: División por cero no permitida."
    else:
        return int(num1 / num2)

res = input("Hola querido usuario. ¿Deseas que haga alguna operación matemática básica (Suma, Resta,",
" Multiplicación o división)?: (si/no)  ").strip().lower()
if res == "si":
    a = float(input("Ingrese primer número: "))
    b = float(input("Ingrese segundo número: "))
    print("¿Qué operación deseas realizar?")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    operacion = int(input("Selecciona una opción (1/2/3/4): "))
    
    if operacion == 1:
        print("Has seleccionado Sumar.")
        print("La suma de los números es: ", sumarNumeros(a, b))
    elif operacion == 2:
        print("Has seleccionado Restar.")
        print("La resta de los números es: ", restarNumeros(a, b))
    elif operacion == 3:
        print("Has seleccionado Multiplicar.")
        print("La multiplicación de los números es: ", multiplicarNumeros(a, b))
    elif operacion == 4:
        print("Has seleccionado Dividir.")
        print("La división de los números es: ", dividirNumeros(a, b))
    else:
        print("Opción no válida. Por favor, selecciona una opción entre 1 y 4.")
        exit()
elif res != "no" or res != "si":
    print("Respuesta no válida. Por favor, responde 'si' o 'no'.")
    exit()
else:
    print("No se realizará ninguna operación.")
    exit()



# Función para el primer ejercicio: calcular el área de un triángulo, cuadrado o circunferencia.

def calcularArea(figura, base, altura, lado, radio):
    if figura == "triángulo" or figura == "triangulo":
        area = (base * altura) / 2
        print()
        print(f"El área del triángulo es: {area}")
    elif figura == "cuadrado":
        area = lado ** 2
        print()
        print(f"El área del cuadrado es: {area}")
    elif figura == "circunferencia":
        area = 3.14 * (radio ** 2)
        print()
        print(f"El área de la circunferencia es: {area}")
        
# Función para el segundo ejercicio: calcular el interés de una suma de dinero.

def calcularInteres(valor_inicial, tasa_interes, tiempo):
    interes = (valor_inicial * tasa_interes * tiempo) / 100
    return f"El interés generado es de {interes}"

# Función para el tercer ejercicio: convertir dólares a pesos y viceversa.

def convertirDivisas(opcion, valorCOP):
    if opcion in (1, 2):
        if opcion == 1:
            cantidadDolares = float(input("Digita la cantidad de dólares que deseas convertir a COP: "))
            valor_final = cantidadDolares * valorCOP
            return f"{cantidadDolares} USD equivale a {valor_final:.2f} COP"
        elif opcion == 2:
            cantidadPesos = float(input("Digita la cantidad de pesos que deseas convertir a USD: "))
            valor_final = cantidadPesos / valorCOP
            return f"{cantidadPesos} COP equivale a {valor_final:.2f} USD"
    else:
        return "Respuesta inválida."

    
# Función para el cuarto ejercicio: calcular el promedio de sueldos.

def calcularPromedioSueldos(sueldos):
    promedio = sum(sueldos) / len(sueldos)
    print(f"El promedio de sueldos es: {promedio:,.2f}")
    
# Función para el quinto ejercicio: calcular la edad de un paciente.

def calcularEdad(año_nacimiento, año_actual):
    return print (f"{nombre_usuario}, tu edad es: {año_actual - año_nacimiento }",  "años")

print("¡Bienvenido!")
nombre_usuario = str(input("¿Cuál es tu nombre?: ")).strip().capitalize()
print()
print(f"Hola {nombre_usuario}, espero que estés teniendo un buen día.")
print("Este programa contiene distintos ejercicios de programación hechos en Python, pasarás uno por uno hasta llegar al último.")
print()

# Ejercicio 1: Crear un programa segun este problema: "En un departamento de matemáticas se necesita un programador que halle el área de un triángulo, área de un cuadrado y área de una circunferencia, además de eleveralo al cubo en el lenguaje de programación "Python".

print("Este es el ejercicio numero 1: El calculador de áreas")
print()

figura = str(input("¿Qué figura deseas calcular el área? (triángulo, cuadrado, circunferencia): ")).strip().lower()
if figura == "triángulo" or figura == "triangulo":
    calcularArea(figura, base=float(input("Ingrese la base del triángulo: ")), altura=float(input("Ingrese la altura del triángulo: ")), lado=0, radio=0)
elif figura == "cuadrado":
    calcularArea(figura, base=0, altura=0, lado=float(input("Ingrese el lado del cuadrado: ")), radio=0)
elif figura == "circunferencia":
    calcularArea(figura, base=0, altura=0, lado=0, radio=float(input("Ingrese el radio de la circunferencia: ")))    
else:
    print("Figura no válida. Por favor, selecciona entre triángulo, cuadrado o circunferencia.")
    exit()

# Ejercicio 2: Crear un programa segun este problema: "En un banco se desea desarrollar un programa que halle el interés de determinada suma en el lenguaje de programación "Python".

print("Este es el ejercicio numero 2: El calculador de intereses")
print()

valor_inicial = float(input("Ingrese el valor inicial: "))
tasa_interes = float(input("Ingrese la tasa de interés (en %): "))
tiempo = float(input("Ingrese el tiempo (en años): "))
interes = calcularInteres(valor_inicial, tasa_interes, tiempo)
print(interes)

# Ejercicio 3: Crear un programa segun este problema: "En un centro de visas se necesita un programa que realice la converisón de dolares a pesos y de pesos a dolares en el lenguaje de programación "Python".

valor_pesos_a_dolar = 4304.38

print("Este es el ejercicio número 3: El convertidor de divisas (COP - Dólar americano)\n")
print("1. Dólares a pesos")
print("2. Pesos a dólares")

try:
    opcion = int(input("Seleccione una opción (1 o 2): "))
    resultado = convertirDivisas(opcion, valor_pesos_a_dolar)
    print(resultado)
except ValueError:
    print("Por favor, ingrese un número válido (1 o 2).")

# Ejercicio 4: Crear un programa segun este problema: "En una departamento de contabilidad se necesita un programa que calcule el promedio de sueldos de un empleado durante un año en el lenguaje de programación "Python".

print("Este es el ejercicio número 4: El calculador de sueldos")
print()

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

sueldos = {mes: float(input(f"Ingrese el sueldo de {mes.lower()}: ")) for mes in meses}

calcularPromedioSueldos(sueldos.values())

# Ejercicio 5: Crear un programa segun este problema: "En un centro médico se necesita un programa que halle la edad de un paciente en el lenguaje de programación "Python".

print("Este es el ejercicio número 5: El calculador de edad")
print()

año_nacimiento =  int(input("Ingrese su año de nacimiento: "))
año_actual = datetime.now().year

calcularEdad(año_nacimiento, año_actual)
print("Gracias por usar el programa. ¡Hasta luego!")
