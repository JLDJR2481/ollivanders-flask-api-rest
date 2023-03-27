from flask import Blueprint, jsonify

root_bp = Blueprint("root", __name__)

@root_bp.route("/", methods=["GET"])
def welcome():
    return jsonify({'Te damos la bienvenida a Ollivanders!': '\nPara ver el inventario, escribe /inventario. \nPara ver un item en concreto, escribe /items/find/id del item'}), 200
