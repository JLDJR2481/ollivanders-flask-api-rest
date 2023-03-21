from data_access.inventarioInicial import *
import pytest

@pytest.mark.inventarioInicial
def test_inventarioIncial():

    inventario = inventario_inicial()

    assert inventario != None
    assert len(inventario) == 9
    assert inventario[0] == {"id": 1, "name": "+5 Dexterity Vest", "sell_in": 10, "quality": 20, "type": "NormalItem"}

    assert inventario[-1] ==     {
      "id": 9,
      "name": "Conjured Mana Cake",
      "sell_in": 3,
      "quality": 6,
      "type": "Conjured"
    }