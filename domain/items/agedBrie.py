from domain.items.normalItem import NormalItem


class AgedBrie(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def setQuality(self, valor):
        NormalItem.setQuality(self, valor)

    def updateQuality(self):
        if self.sell_in > 0:
            self.setQuality(1)

        else:
            self.setQuality(2)

        self.setSellIn()
