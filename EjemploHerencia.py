from abc import ABC,abstractmethod

class Animal(ABC):
    nombre:str=""
    def __init__(self,nombreDado:str):
        self.nombre=nombreDado
    @abstractmethod
    def mellamo(self):
        NotImplementedError
            
    @abstractmethod
    def habla(self):
        pass
class Perro(Animal):
    def __init__(self, nombreDado:str):
        super().__init__(nombreDado)
    def habla(self):
        print("guau guau")
        def yocomo(self,comida:str):
            print("pollo")  
        def mellamo(self):
            return self.nombre     
        
class Gato(Animal):
    def habla(self):
        print("miau miau")
        def yocomo(self,comida:str):
            print("croquetas")
        def mellamo(self):
            return self.nombre 
        
class Rana(Animal):
    def habla(self):
        print("ranac ranac")
        def yocomo(self,comida:str):
            print("Insectos")   
        def mellamo(self):
            return self.nombre      
#creacion de objetos polimórficos
obj:Animal
obj=Perro("scobydoo")
obj.habla()
print(f"llamame")

obj=Gato()
obj.habla()

obj:Animal
obj=Rana()
obj.habla()