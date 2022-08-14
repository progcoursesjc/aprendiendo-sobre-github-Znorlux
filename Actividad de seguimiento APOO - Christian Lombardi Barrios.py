#Clase de parciales
class Parciales:
    def __init__(self, nombre_curso, porcentaje, lista_preguntas):
        self.nombre_curso = nombre_curso
        self.porcentaje = porcentaje
        self.lista_preguntas = lista_preguntas
#Listas, en lista_parciales se guardara el resultado del usuario  
lista_parciales = []
lista_cursos = ["1. Matematicas", 
                "2. Ingles", 
                "3. Fisica", 
                "4. Quimica",
                "5. Literatura"]

#Funcion para mostrar el resultado hecho por el usuario             
def Mostrar():
   j=0
   while j<len(lista_parciales):
        print(lista_parciales[j].nombre_curso," - Porcentaje:",lista_parciales[j].porcentaje,"%")
        for r in lista_parciales[j].lista_preguntas:
            print("Pregunta:",r)
        j+=1
#Funcion para crear objeto "parcial" y asignarle sus respectivos atributos a una lista        
def crear_parcial():
    n_curso = k #Esta variable asigna el curso que fue seleccionado en la lista para luego ser enviado a la clase
    porcentaje_parcial = int(input("Ingrese el porcentaje que tendra el parcial: "))
    n_preguntas = int(input("Ingrese el número de preguntas que tendrá el parcial: "))
    print("Ingrese las preguntas del parcial, una por una: ")
    l_preguntas = []
    for n in range(n_preguntas):
        preguntas = str(input())
        l_preguntas.append(preguntas)
        
    parcial = Parciales(n_curso, porcentaje_parcial, l_preguntas)
    lista_parciales.append(parcial)
    
    print("Parcial guardado con exito!")
    print("A continuación, el resultado:")
    print("================")
    Mostrar()

    #PROGRAMA PRINCIPAL
print("Bienvenido al programa de creacion de parciales!")
print("Lista de cursos: ")
print("================")
for i in lista_cursos:
    print(i)
print("================")
curso = int(input("Seleccione un curso según su número: "))
if curso == 1:
    k = lista_cursos[0]
    crear_parcial()
elif curso == 2:
    k = lista_cursos[1]
    crear_parcial()
elif curso == 3:
    k = lista_cursos[2]
    crear_parcial()
elif curso == 4:
    k = lista_cursos[3]
    crear_parcial()
elif curso == 5:
    k = lista_cursos[4]
    crear_parcial()
else:
    while curso < 1 or curso > 5:
        print("Opción invalida, por favor ingrese un curso valido")
        curso = int(input("Seleccione un curso: "))
        if curso == 1:
            k = lista_cursos[0]
            crear_parcial()
        elif curso == 2:
            k = lista_cursos[1]
            crear_parcial()
        elif curso == 3:
            k = lista_cursos[2]
            crear_parcial()
        elif curso == 4:
            k = lista_cursos[3]
            crear_parcial()
        elif curso == 5:
            k = lista_cursos[4]
            crear_parcial()
    

        


    
      


    
        
    


    

    
    
        
    
   

    

    
    
    
    
    
    