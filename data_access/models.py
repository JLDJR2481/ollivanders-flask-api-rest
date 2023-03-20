from mongoengine import Document, StringField, IntField

class Item(Document):
    id = IntField(required=True)
    name = StringField(required=True)
    sell_in = IntField(required=True)
    quality = IntField(required=True)
    item_type = StringField(required=True)