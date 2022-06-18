
import os
from flask import Flask, jsonify, request
from models import db, Usuario, Favorito, Episodio, Personaje
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate



BASEDIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
#configs
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASEDIR, "api_test.db")
app.config["DEBUG"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
CORS(app)
Migrate(app, db)



#°[POST]°[POST]°[POST]°[POST]°[POST]°[POST]°[POST](CREA)
@app.route("/un_usuario", methods=["POST"])   
def un_usuario():
    un_usuario = Usuario()
    un_usuario.id = request.json.get("id")
    un_usuario.nombre = request.json.get("nombre")
    un_usuario.nombre_usuario = request.json.get("nombre_usuario")
    un_usuario.email = request.json.get("email")
    un_usuario.favorito = request.json.get("favorito")

    db.session.add(un_usuario)
    db.session.commit()  

    return jsonify(un_usuario.serialize()), 200



#°[GET]°[GET]°[GET]°[GET]°[GET]°[GET]°[GET]°[GET](OBTIENE)
@app.route("/todos_los_usuarios", methods=["GET"])
def todos_los_usuarios():
    todos_los_usuarios = Usuario.query.all()
    todos_los_usuarios = list(map(lambda x: x.serialize(), todos_los_usuarios))
    return jsonify(todos_los_usuarios)



#°[PUT]°[PUT]°[PUT]°[PUT]°[PUT]°[PUT]°[PUT]°[PUT](ACTUALIZA)
@app.route("/un_usuario/<int:id>",  methods=["PUT"])
def config_usuario(id):
    un_usuario = Usuario.query.get(id)
    print(un_usuario.nombre_usuario, "antiguo")
    un_usuario.nombre_usuario = request.json.get("nombre_usuario")
    print(un_usuario.nombre_usuario, "nuevo")

    db.session.commit()

    return jsonify(un_usuario.serialize())



#°[DELETE]°[DELETE]°[DELETE]°[DELETE]°[DELETE](ELIMINA)
@app.route("/un_usuario/<int:id>", methods=["DELETE"])
def eliminar(id):
    un_usuario = Usuario.query.get(id)

    db.session.delete(un_usuario)

    return jsonify({"eliminado": True}), 200


if __name__ == "__main__":
    app.run(host="localhost", port="5000")
