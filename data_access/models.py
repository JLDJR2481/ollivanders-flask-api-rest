from domain.items.normalItem import NormalItem
from domain.items.agedBrie import AgedBrie
from domain.items.backstage import Backstage
from domain.items.conjured import Conjured
from domain.items.sulfuras import Sulfuras


class Item:
    def __init__(self, _id, name, sell_in, quality, item_type):
        self._id = _id
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.item_type = item_type

    def updateItem(self):
        item = eval(self.item_type)(self.name, self.sell_in, self.quality)

        item.updateQuality()

        return {"sell_in": item.sell_in, "quality": item.quality}
