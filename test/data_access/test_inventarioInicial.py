from data_access.inventarioInicial import *
from data_access.database import Database
import pytest


@pytest.mark.inventarioInicial
def test_inventarioIncial():
    Database.initdb()
    inventario = inventario_inicial()

    assert inventario != None
    assert len(inventario) == 9
    assert inventario[0] == {
        "_id": 1,
        "name": "+5 Dexterity Vest",
        "sell_in": 10,
        "quality": 20,
        "item_type": "NormalItem",
    }

    assert inventario[-1] == {
        "_id": 9,
        "name": "Conjured Mana Cake",
        "sell_in": 3,
        "quality": 6,
        "item_type": "Conjured",
    }

    Database.dropCollection()
