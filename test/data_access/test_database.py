from data_access.database import Database
import pytest


@pytest.mark.initDatabase
def test_initdb():
    Database.dropCollection()

    Database.initdb()
    assert Database.collection.count_documents({}) == 9

    Database.dropCollection()
    assert Database.collection.count_documents({}) == 0


@pytest.mark.createItem
def test_createItem():
    Database.dropCollection()

    item = {
        "_id": 1,
        "name": "+5 Dexterity Vest",
        "sell_in": 10,
        "quality": 20,
        "type": "NormalItem",
    }
    assert Database.createItem(item).inserted_id == 1


@pytest.mark.readItem
def test_readItem():
    assert Database.readItem(1)["name"] == "+5 Dexterity Vest"


@pytest.mark.updateItem
def test_updateItem():
    assert Database.updateItem(1, {"name": "+5 Strength Sword"}).modified_count == 1
    assert Database.readItem(1)["name"] == "+5 Strength Sword"


@pytest.mark.deleteItem
def test_deleteItem():
    assert Database.deleteItem(1).deleted_count == 1


@pytest.mark.inventario
def test_inventario():
    Database.initdb()

    inventario = Database.inventario()

    assert isinstance(inventario, list)
    assert len(inventario) == 9

    for item in inventario:
        assert "_id" in item
        assert "name" in item
        assert "sell_in" in item
        assert "quality" in item
        assert "item_type" in item

    Database.dropCollection()
