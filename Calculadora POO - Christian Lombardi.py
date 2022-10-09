
class Division0Error(Exception):
    pass

class Calculadora:
    def __init__(self):
        self.resultado = 0
    
    def ingresar_datos(self):
        try:
            valor=input("Ingrese numeros y operacion a realizar: ")
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
                except ZeroDivisionError:
                    print("No puedes dividir por 0, vuelve a intentarlo")
                    self.ingresar_datos()
                except ValueError:
                    print("Solo puedes ingresar valores numericos")
                    self.ingresar_datos()
    
                
c = Calculadora()
c.ingresar_datos()
