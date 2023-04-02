from flask import Blueprint, request, jsonify
from services.services import *

items_blueprint = Blueprint("items", __name__)


@items_blueprint.route("/items", methods=["GET"])
def welcomeItem():
    return (
        jsonify(
            {
                "Bienvenido a la seccion de items!": "Puedes realizar 4 operaciones: Crear un item con /create. Buscar un item con /find/id. Debes insertar una id. Updatear un item con /update/id. Debes insertar una id. Borrar un item de la base de datos con /delete/id. Debes insertar una id."
            }
        ),
        200,
    )


@items_blueprint.route("/items/create", methods=["POST"])
def createItem():
    item = request.json

    required_keys = ["_id", "name", "sell_in", "quality", "item_type"]

    if not all(key in item for key in required_keys):
        return jsonify({"ERROR": "Faltan algunas claves"}), 400

    else:
        if Services.readItem(item["_id"]) == None:
            resultado = Services.createItem(item)
            return jsonify({"Se ha creado un item con id": resultado.inserted_id}), 201

        else:
            return (
                jsonify(
                    {
                        "ERROR": "Ya existe un item en el inventario con ese id. Introduzca una id distinta"
                    }
                ),
                400,
            )


@items_blueprint.route("/items/find/<id>", methods=["GET"])
def readItem(id):
    try:
        resultado = Services.readItem(int(id))
    except ValueError:
        return jsonify({"ERROR": "Se ha introducido un valor incorrecto"}), 400

    if resultado is None:
        return jsonify({"ERROR": "No se ha podido encontrar el item con la id"}), 404
    else:
        return jsonify({"Aqui tienes el item: ": resultado}), 200


@items_blueprint.route("/items/update/<id>", methods=["PUT"])
def updateItem(id):
    try:
        item_id = int(id)
    except ValueError:
        return jsonify({"ERROR": "No se ha introducido un numero"}), 400

    if Services.readItem(item_id) is None:
        return (
            jsonify({"ERROR": "No se ha encontrado un item con la id correspondiente"}),
            404,
        )

    resultado = Services.updateItem(item_id, request.json)

    if resultado.modified_count == 1:
        return jsonify({"Se ha actualizado el item con el id ": id}), 200


@items_blueprint.route("/items/delete/<id>", methods=["DELETE"])
def deleteItem(id):
    try:
        item_id = int(id)
    except ValueError:
        return jsonify({"ERROR": "La id introducida no es valida"}), 400

    if Services.readItem(item_id) is None:
        return (
            jsonify(
                {"ERROR": "No se ha encontrado un item con la id correspondiente."}
            ),
            404,
        )

    result = Services.deleteItem(item_id)

    if result.deleted_count == 1:
        return jsonify({"Se ha eliminado el item con el id ": str(item_id)}), 200
