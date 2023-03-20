import json
from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
api = Api(app)

with open('docs/inventario.json', 'r+') as f:
    inventario = json.load(f)["inventory"]

@app.route('/', methods=['GET'])
def welcome():
    return 'Prueba de welcome!'

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return json.dumps(inventario)

@app.route('/inventory/<name>', methods=['GET'])
def get_single_item(name):
    name = name.lower()
    for item in inventario:
        if item["name"].lower() == name:
            return {'Name: ' : item['name'],
                    'Sell_in: ' : item['sell_in'], 
                    'Quality: ' : item['quality']}
        
    return 'El item esperado no se encuentra en el inventario', 404


@app.route('/update', methods=['GET'])
def update_inventario():
    for item in inventario:
        item['sell_in'] -= 1
        item['quality'] -= 1
    
    with open('inventario.json', 'w') as f:
        json.dump({'items': inventario}, f, indent=4)

    return 'Se ha actualizado el inventario correctamente'

@app.route('/update/<name>', methods=['GET'])
def update_item(name):
    name = name.lower()
    for item in inventario:
        if item["name"].lower() == name:
            item['sell_in'] -= 1
            item['quality'] -= 1
            with open('inventario.json', 'w') as f:
                json.dump({'items': inventario}, f, indent=4)
            return 'Se ha actualizado el item llamado {nombre} correctamente'.format(nombre=name)

    return 'No se ha encontrado el item que se desea actualizar' , 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
