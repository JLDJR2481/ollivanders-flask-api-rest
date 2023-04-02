from domain.items.normalItem import NormalItem


class Backstage(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def setQuality(self, valor):
        NormalItem.setQuality(self, valor)

    def updateQuality(self):
        if self.sell_in > 10:
            self.setQuality(1)

        elif self.sell_in > 5:
            self.setQuality(2)

        elif self.sell_in > 0:
            self.setQuality(3)

        else:
            self.quality = 0

        self.setSellIn()
