from unicodedata import name

class Person: #Clase base
    def __init__(self, name, age, size, hair_color):
        self.name: str = name
        self.age: int = age
        self.size: float = size
        self.hair_color: str= hair_color

    def Walk(self, distance: int) -> str:

        return f"Soy {self.name} y voy a recorrer {distance} metros"

    def Eat(self, food: str) -> str:

        return f"Soy {self.name} y hoy voy a comer {food}"

    def Speak(self, language: str) -> str: 
        return f"Mi nombre es {self.name} y hablo {language}"
        

class Student(Person): #Clase derivada
    def Study(self, subject: str) ->str:
        return f"Soy {self.name} y voy a estudiar {subject}"

class Teacher(Person): #Clase derivada
    def Teach(self, subject: str) -> str:
        return f"Mi nombre es {self.name} y hoy les voy a enseñar sobre {subject}"
    
s1 = Student("Juan", 16, 1.70, "negro")
t1 = Teacher("Gildardo", 51, 1.85, "gris")

print(s1.Walk(10)) #Prueba de metodo Walk para Student
print(t1.Walk(25)) #Preuba de metodo Walk para Teacher
print("=="*20)

print(s1.Eat("manzana")) #Prueba de metodo Eat
print("=="*20)

print(t1.Speak("Español")) #Prueba de metodo Speak
print("=="*20)

print(s1.Study("Matematicas")) #Prueba de metodo Study solo valido para la clase Student
print(t1.Teach("Calculo")) #Prueba de metodo Teach solo valido para la clase Teacher


