import json


def inventario_inicial():
    with open("docs/inventario.json") as f:
        inventario = json.load(f)

    return inventario["inventory"]
