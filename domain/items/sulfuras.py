from domain.items.normalItem import NormalItem


class Sulfuras(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def updateQuality(self):
        assert self.quality == 80
        pass
