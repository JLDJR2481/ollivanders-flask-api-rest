class Interfaz():

    def updateQuality(self):
        pass


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "{}, {}, {}".format(self.name, self.sell_in, self.quality)


class NormalItem(Item, Interfaz):

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


class AgedBrie(NormalItem):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def setQuality(self, valor):
        NormalItem.setQuality(self, valor)

    def updateQuality(self):
        if self.sell_in > 0:
            self.setQuality(1)

        else:
            self.setQuality(2)

        self.setSellIn()


class Sulfuras(NormalItem):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def updateQuality(self):
        assert self.quality == 80
        pass


class Conjured(NormalItem):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def updateQuality(self):
        if self.sell_in >= 0:
            self.setQuality(-2)
        else:
            self.setQuality(-4)

        self.setSellIn()


class Backstage(NormalItem):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

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
