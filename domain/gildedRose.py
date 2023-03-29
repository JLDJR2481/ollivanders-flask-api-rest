class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def updateInventory(self):
        for item in self.items:
            item.updateQuality()
