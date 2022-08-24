import datetime
from datetime import date, time, datetime

class Producto:
    def __init__(self, id, nombre, precio: int):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.historial_precio = dict = {date:precio}


class Usuario:
    def __init__(self, id: int, nombre_usuario):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.balance = 0
        self.lista_orden = []

carrito_compras = []
usuario1 = Usuario(1, "Christian Lombardi",)
print(f"Bienvenido {usuario1.nombre_usuario}, su saldo actual es {usuario1.balance}")

class Orden:
    def __init__(self, id, lista_productos):
        self.id = id
        self.lista_productos = lista_productos
        self.fecha = date
        self.total = float
        self.estado = bool
    

#Funcion para la creacion de los productos y para añadirlos al carrito de compras
def añadir_producto():
    
    producto1 = Producto(1, "Platano", 1200)
    producto2 = Producto(2, "Manzana", 1000)
    producto3 = Producto(3, "Arroz", 2500)
    producto4 = Producto(4, "Lechuga", 1300)
    carrito_compras.append(producto1)
    carrito_compras.append(producto2)
    carrito_compras.append(producto3)
    carrito_compras.append(producto4)
    j=0
    while j<len(carrito_compras):
        print(carrito_compras[j].id," Producto:",carrito_compras[j].nombre, "- Precio:", carrito_compras[j].precio,"$")
        j+=1
añadir_producto()

def añadir_balance():
        usuario1.balance = 6500
        print(f"Su saldo actual ahora es de {usuario1.balance}")
añadir_balance()
#Creacion del objeto tipo Orden donde se guardaran todos los productos
orden1 = Orden(1, carrito_compras)

def consolidar_orden():
    #Suma del valor de los productos:
    valor_total= int(orden1.lista_productos[0].precio + orden1.lista_productos[1].precio + orden1.lista_productos[2].precio + orden1.lista_productos[3].precio)
    print(f"El valor total de sus productos es {valor_total}")

    if usuario1.balance < valor_total:
        print("Saldo insuficiente")
    else:
        usuario1.balance -= valor_total
        print(f"Compra finalizada,su saldo actual ahora es {usuario1.balance} $ desea volver a comprar nuevos productos?" )
        opcion = int(input("No = 0 - Si = 1: "))
        if opcion == 1:
            carrito_compras.clear()
            añadir_producto()
            añadir_balance()
            consolidar_orden()
        elif opcion == 0:
            print("Gracias por su compra")
            exit()
            
            
consolidar_orden()