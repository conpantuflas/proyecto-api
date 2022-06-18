from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    nombre_usuario = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    favorito = db.Column(db.Integer)

    #db.ForeignKey("favoritos.id")


    def __repr__(self):
        return "<Usuario %r" % self.email

    def serialize(self):
        return {
            "id": self.id,
            "nombre" : self.nombre,
            "nombre_usuario": self.nombre_usuario,
            "email": self.email,
            "favorito" : self.favorito
        }    


class Favorito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    personaje = db.Column(db.String(100), unique=True)
    episodio = db.Column(db.String(100), unique=True)


    def __repr__(self):
        return "<Favorito %r" % self.id

    def serialize(self):
        return {
            "id": self.id,
            "personaje" : self.personaje,
            "episodio": self.episodio
        } 


class Episodio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True)
    air_date = db.Column(db.String(50))
    episode = db.Column(db.String(50))

    def __repr__(self):
        return "<Episodio %r" % self.nombre

    def serialize(self):
        return {
            "id": self.id,
            "nombre" : self.nombre,
            "air_date": self.air_date,
            "episode": self.episode,
        }    



class Personaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True)
    status = db.Column(db.String(50))
    species = db.Column(db.String(50))

    def __repr__(self):
        return "<Personaje %r" % self.nombre

    def serialize(self):
        return {
            "id": self.id,
            "nombre" : self.nombre,
            "status": self.status,
            "species": self.species
        }                  