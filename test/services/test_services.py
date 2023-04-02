import unittest
from data_access.database import Database
from services.services import Services
import pytest


class TestService(unittest.TestCase):
    def setUp(self):
        Database.initdb()

    def tearDown(self):
        Database.dropCollection()

    @pytest.mark.createItemSer
    def test_createItem(self):
        item = {
            "_id": 10,
            "name": "Item Test name",
            "sell_in": 10,
            "quality": 10,
            "item_type": "NormalItem",
        }

        result = Services.createItem(item)
        self.assertIsNotNone(result)
        self.assertEqual(result.inserted_id, 10)

    @pytest.mark.readItemSer
    def test_readItem(self):
        item = {
            "_id": 10,
            "name": "Item Test name",
            "sell_in": 10,
            "quality": 10,
            "item_type": "NormalItem",
        }
        Services.createItem(item)

        result = Services.readItem(10)

        self.assertIsNotNone(result)
        self.assertEqual(result["_id"], 10)
        self.assertEqual(result["name"], "Item Test name")

    @pytest.mark.updateItemSer
    def test_updateItem(self):
        item = {
            "_id": 10,
            "name": "Item Test name",
            "sell_in": 10,
            "quality": 10,
            "item_type": "NormalItem",
        }

        Services.createItem(item)

        old_result = Services.readItem(10)

        update_statement = {"quality": 20}

        update_result = Services.updateItem(10, update_statement)

        self.assertIsNotNone(update_result)
        self.assertEqual(update_result.modified_count, 1)
        self.assertNotEqual(Services.readItem(10)["quality"], old_result["quality"])
        self.assertEqual(Services.readItem(10)["quality"], 20)

    @pytest.mark.deleteItemSer
    def test_deleteItem(self):
        item = {
            "_id": 10,
            "name": "Item Test name",
            "sell_in": 10,
            "quality": 10,
            "item_type": "NormalItem",
        }

        Services.createItem(item)
        result = Services.deleteItem(10)

        self.assertIsNotNone(result)
        self.assertEqual(result.deleted_count, 1)
        self.assertIsNone(Services.readItem(10))

    @pytest.mark.inventarioSer
    def test_inventario(self):
        item = {
            "_id": 10,
            "name": "Item Test name",
            "sell_in": 10,
            "quality": 10,
            "item_type": "NormalItem",
        }

        Services.createItem(item)
        result = Services.inventario()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

        self.assertIn(item, result)
