from flask import Flask
import pytest
from resources.inventario import inventario_bp
from services.services import Services
from data_access.database import Database


@pytest.fixture
def client():
    Database.initdb()
    app = Flask(__name__)
    app.register_blueprint(inventario_bp)
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client
    Database.dropCollection()


@pytest.mark.inventarioRes
def test_get_inventario(client):
    response = client.get("/inventario")

    item = {
        "_id": 1,
        "name": "+5 Dexterity Vest",
        "sell_in": 10,
        "quality": 20,
        "item_type": "NormalItem",
    }

    assert response.status_code == 200
    assert item in response.json


@pytest.mark.updateInventarioRes
def test_update_inventario(client):
    response = client.get("/inventario/update")
    item = {
        "_id": 1,
        "name": "+5 Dexterity Vest",
        "sell_in": 9,
        "quality": 19,
        "item_type": "NormalItem",
    }

    assert response.status_code == 200
    assert item in response.json
