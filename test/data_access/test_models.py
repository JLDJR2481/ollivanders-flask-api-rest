from data_access.models import Item

from domain.items import *

import pytest


@pytest.fixture
def initItems():
    normal = Item(1, "+5 Dexterity Vest", 10, 20, "NormalItem")
    agedBrie = Item(2, "Aged Brie", 2, 0, "AgedBrie")
    sulfur = Item(3, "Sulfuras, Hand of Ragnaros", 0, 80, "Sulfuras")
    backstage = Item(
        4, "Backstage passes to a TAFKAL80ETC concert", 15, 20, "Backstage"
    )
    conjured = Item(5, "Conjured Mana Cake", 3, 6, "Conjured")

    return [normal, agedBrie, sulfur, backstage, conjured]


@pytest.mark.updateNormal
def test_updateNormal(initItems):
    item = initItems[0]

    assert item.updateItem() == {"sell_in": 9, "quality": 19}


@pytest.mark.updateBrie
def test_updateBrie(initItems):
    item = initItems[1]

    assert item.updateItem() == {"sell_in": 1, "quality": 1}


@pytest.mark.updateSulfuras
def test_updateSulfuras(initItems):
    item = initItems[2]

    assert item.updateItem() == {"sell_in": 0, "quality": 80}


@pytest.mark.updateBackstage
def test_updateBackstage(initItems):
    item = initItems[3]

    assert item.updateItem() == {"sell_in": 14, "quality": 21}


@pytest.mark.updateConjured
def test_updateConjured(initItems):
    item = initItems[4]

    assert item.updateItem() == {"sell_in": 2, "quality": 4}
