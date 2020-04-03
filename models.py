from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy() #objeto de referencia

class Contact(db.Model): # crea una tabla de contactos
    __tablename__ = "contacts"
    id = db.Column(db.Integer, primary_key=True) # el valor se genera automatica%
    name = db.Column(db.String(100), nullable=False) # el nombre va a ser obligatorio
    phone = db.Column(db.String(100), nullable=False) # el telefono va a ser obligatorio

    def serialize(self): # cambiar el objeto python a JSON
        # son los datos q devuelve de la tabla
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone
        }