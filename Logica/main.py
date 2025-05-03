def peticion():
    numero1 = float(input("ingresar el primer numero: "))
    numero2 = float(input("ingresar el segundo numero: "))
    return numero1, numero2

def sumar(numero1, numero2):
    return numero1 + numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2


operacion = input("que operacion quieres realizar?(sumar => s /multiplicar => x): ")


num1 , num2 =peticion()


if operacion == "s":
    resultado = sumar(num1, num2)
    print("el resultado de la suma es: ",resultado)
elif operacion == "x":
    resultado = multiplicar(num1, num2)
    print("el resultado de la multiplicacion es: ",resultado)
else:
    print("Operacion no valida")
