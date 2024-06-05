''' from abc import ABC,abstractmethod

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
obj.habla() '''

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

class User(BaseModel):
    __tablename__ = 'users'
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return f'<User {self.name}>'

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

if __name__ == '__main__':
    db.create_all()  # Crea las tablas si no existen
    app.run(debug=True)
