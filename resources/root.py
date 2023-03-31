from flask import Blueprint, jsonify

root_bp = Blueprint("root", __name__)


@root_bp.route("/", methods=["GET"])
def welcome():
    return (
        jsonify(
            {
                "Te damos la bienvenida a Ollivanders!": "Para ver el inventario, escribe /inventario. Para ver un item en concreto, escribe /items/find/id del item"
            }
        ),
        200,
    )
