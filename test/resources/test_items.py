from services.services import *
from flask import Flask
from resources.items import items_blueprint
import pytest


@pytest.fixture
def client():
    if Services.readItem(10):
        Services.deleteItem(10)

    app = Flask(__name__)
    app.register_blueprint(items_blueprint)
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


@pytest.mark.welcomeItemRes
def test_welcomeItem(client):
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json == {
        "Bienvenido a la seccion de items!": "Puedes realizar 4 operaciones: Crear un item con /create. Buscar un item con /find/id. Debes insertar una id. Updatear un item con /update/id. Debes insertar una id. Borrar un item de la base de datos con /delete/id. Debes insertar una id."
    }


@pytest.mark.createItemRes
def test_createItem(client):
    first_item = {
        "_id": 10,
        "name": "Espada de Griffindor",
        "sell_in": 20,
        "quality": 10,
        "item_type": "NormalItem",
    }

    response = client.post("/items/create", json=first_item)

    assert response.status_code == 201
    assert response.json == {"Se ha creado un item con id": 10}

    second_item = {
        "_id": 10,
        "name": "Espada de Griffindor",
        "sell_in": 20,
        "item_type": "NormalItem",
    }

    response = client.post("/items/create", json=second_item)

    assert response.status_code == 400
    assert response.json == {"ERROR": "Faltan algunas claves"}

    third_item = {
        "_id": 10,
        "name": "Espada de Griffindor",
        "sell_in": 20,
        "quality": 10,
        "item_type": "NormalItem",
    }

    response = client.post("/items/create", json=third_item)

    assert response.status_code == 400
    assert response.json == {
        "ERROR": "Ya existe un item en el inventario con ese id. Introduzca una id distinta"
    }


@pytest.mark.readItemRes
def test_readItem(client):
    item = {
        "_id": 10,
        "name": "Espada de Griffindor",
        "sell_in": 20,
        "quality": 10,
        "item_type": "NormalItem",
    }

    Services.createItem(item)

    response = client.get("/items/find/10")

    assert response.status_code == 200
    assert response.json == {"Aqui tienes el item: ": item}

    Services.deleteItem(10)

    response = client.get("/items/find/no_un_id")

    assert response.status_code == 400
    assert response.json == {"ERROR": "Se ha introducido un valor incorrecto"}

    response = client.get("/items/find/10")
    assert response.status_code == 404
    assert response.json == {"ERROR": "No se ha podido encontrar el item con la id"}


@pytest.mark.updateItemRes
def test_updateItem(client):
    item = {
        "_id": 10,
        "name": "Espada de Griffindor",
        "sell_in": 20,
        "quality": 10,
        "item_type": "NormalItem",
    }

    Services.createItem(item)

    update_statement = {"quality": 8}

    response = client.put("/items/update/10", json=update_statement)

    assert response.status_code == 200
    assert response.json == {"Se ha actualizado el item con el id ": "10"}

    Services.deleteItem(10)

    response = client.put("/items/update/no_una_id", json=update_statement)

    assert response.status_code == 400
    assert response.json == {"ERROR": "No se ha introducido un numero"}

    response = client.put("/items/update/10", json=update_statement)

    assert response.status_code == 404
    assert response.json == {
        "ERROR": "No se ha encontrado un item con la id correspondiente"
    }


@pytest.mark.deleteItemRes
def test_deleteItem(client):
    item = {
        "_id": 10,
        "name": "Espada de Griffindor",
        "sell_in": 20,
        "quality": 10,
        "item_type": "NormalItem",
    }

    Services.createItem(item)

    response = client.delete("/items/delete/10")

    assert response.status_code == 200
    assert response.json == {"Se ha eliminado el item con el id ": "10"}

    response = client.delete("/items/delete/no_un_id")

    assert response.status_code == 400
    assert response.json == {"ERROR": "La id introducida no es valida"}

    response = client.delete("/items/delete/10")

    assert response.status_code == 404
    assert response.json == {
        "ERROR": "No se ha encontrado un item con la id correspondiente."
    }
