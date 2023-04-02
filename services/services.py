from data_access.database import Database


class Services:
    @staticmethod
    def createItem(item):
        return Database.createItem(item)

    @staticmethod
    def readItem(id):
        return Database.readItem(id)

    @staticmethod
    def updateItem(id, update_statement):
        return Database.updateItem(id, update_statement)

    @staticmethod
    def deleteItem(id):
        return Database.deleteItem(id)

    @staticmethod
    def inventario():
        return Database.inventario()
