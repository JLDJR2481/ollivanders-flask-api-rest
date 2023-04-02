from domain.items.item import Item


class NormalItem(Item):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def setSellIn(self):
        self.sell_in = self.sell_in - 1

    def setQuality(self, valor):
        self.quality += valor

        if self.quality > 50:
            self.quality = 50

        elif self.quality < 0:
            self.quality = 0

        assert 50 >= self.quality >= 0

    def updateQuality(self):
        if self.sell_in >= 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)

        self.setSellIn()
