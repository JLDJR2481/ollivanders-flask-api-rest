from flask import Flask
from resources.root import root_bp
import pytest


@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(root_bp)
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


@pytest.mark.welcomeRoot
def test_welcomeRoot(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json == {
        "Te damos la bienvenida a Ollivanders!": "Para ver el inventario, escribe /inventario. Para ver un item en concreto, escribe /items/find/id del item"
    }
