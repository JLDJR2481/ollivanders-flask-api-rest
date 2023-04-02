from domain.items.normalItem import NormalItem
import pytest


@pytest.fixture
def normal_chest():
    test_normal_chest = NormalItem("+5 iron chest", 10, 20)

    return test_normal_chest


@pytest.mark.normalItems
def test_updateQuality(normal_chest):
    test_sell_in = 10
    test_quality = 20

    for i in range(0, 20):
        if test_sell_in < 0:
            test_quality -= 2

        elif test_sell_in >= 0:
            test_quality -= 1

        if test_quality <= 0:
            test_quality = 0

        normal_chest.updateQuality()
        test_sell_in -= 1

        assert normal_chest.quality == test_quality
        assert normal_chest.sell_in == test_sell_in
