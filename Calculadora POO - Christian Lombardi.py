
class Division0Error(ZeroDivisionError):
    pass
class ValorIncorrecto(ValueError):
    pass
class Digito_incorrecto(Exception):
    pass
 
class Calculadora:
    def __init__(self):
        self.resultado = 0
    
    def ingresar_datos(self):
        try:
            valor= input("Ingrese numeros y operacion a realizar: ")
            operador1 = all(element.isdigit() for element in valor.split()[0])
            operador2 = all(element.isdigit() for element in valor.split()[2])
            if operador1 == False:
                print("Debes ingresar un numero en el primer operador")
                c.ingresar_datos()
            elif operador2 == False:
                print("Debes ingresar un numero en el segundo operador")
                c.ingresar_datos()

            print("Si desea terminar la calculadora escriba terminar")
            valor=valor.lower()
            Calculadora.operar(valor,self)
        except:
            if len(valor.split()) != 3:
                print("Debes ingresar dos numeros separados y su operador")
                c.ingresar_datos()

    def operar(valor,self):
            if valor != "terminar":
                try:
                    if valor.split()[1] == "+":
                        self.resultado = int(valor.split()[0]) + int(valor.split()[2])
                        print(f"El resultado de la operacion es {self.resultado:.2f}")
                        self.ingresar_datos()
                    elif valor.split()[1] == "-":
                        self.resultado = int(valor.split()[0]) - int(valor.split()[2])
                        print(f"El resultado de la operacion es {self.resultado:.2f}")
                        self.ingresar_datos()
                    elif valor.split()[1] == "*":
                        self.resultado = int(valor.split()[0]) * int(valor.split()[2])
                        print(f"El resultado de la operacion es {self.resultado:.2f}")
                        self.ingresar_datos()
                    elif valor.split()[1] == "/":
                        self.resultado = int(valor.split()[0]) / int(valor.split()[2])
                        print(f"El resultado de la operacion es {self.resultado:.2f}")
                        self.ingresar_datos()
                except ValorIncorrecto:
                    print("Solo puedes ingresar valores numericos")
                    self.ingresar_datos()
                except Division0Error:
                    print("No puedes dividir por 0, vuelve a intentarlo")
                    self.ingresar_datos()
                
c = Calculadora()
c.ingresar_datos()
