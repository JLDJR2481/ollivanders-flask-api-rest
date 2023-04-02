from flask import Flask
from flask_cors import CORS

from data_access.database import Database
from resources.root import root_bp
from resources.inventario import inventario_bp
from resources.items import items_blueprint


def init_app():
    app = Flask(__name__)
    CORS(app)
    Database.dropCollection()
    Database.initdb()

    app.register_blueprint(root_bp)
    app.register_blueprint(inventario_bp)
    app.register_blueprint(items_blueprint)

    return app


if __name__ == "__main__":
    init_app().run(host="0.0.0.0")
