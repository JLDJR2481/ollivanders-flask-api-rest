from flask import Blueprint, jsonify
from services.services import Services
from data_access.models import Item


inventario_bp = Blueprint("inventario", __name__)


@inventario_bp.route("/inventario", methods=["GET"])
def get_inventario():
    inventario = Services.inventario()
    return jsonify(inventario), 200


@inventario_bp.route("/inventario/update", methods=["GET"])
def updateInventario():
    inventario = Services.inventario()
    for item in inventario:
        item_a_objeto = Item(
            item["_id"],
            item["name"],
            item["sell_in"],
            item["quality"],
            item["item_type"],
        )

        # Services.updateItem(id, update_statement)
        # item_a_objeto.updateItem(). Update de Item
        Services.updateItem(item["_id"], item_a_objeto.updateItem())

    inventario = Services.inventario()

    return jsonify(inventario), 200
