from domain.items.agedBrie import AgedBrie
import pytest


@pytest.fixture
def brie():
    test_brie = AgedBrie("Aged Brie", 2, -2)

    return test_brie


@pytest.mark.agedBrie
def test_updateQuality(brie):
    test_sell_in = 2
    test_quality = -2

    for i in range(0, 12):
        if test_sell_in > 0:
            test_quality += 1

        elif test_sell_in <= 0:
            test_quality += 2

        if test_quality < 0:
            test_quality = 0

        brie.updateQuality()
        test_sell_in -= 1

        assert brie.sell_in == test_sell_in

        assert brie.quality == test_quality
