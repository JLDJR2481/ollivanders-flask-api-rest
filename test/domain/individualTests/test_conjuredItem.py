from domain.items.conjured import Conjured
import pytest


@pytest.fixture
def conjured_sword():
    test_conjured_sword = Conjured("Conjured sword", 18, 40)

    return test_conjured_sword


@pytest.mark.conjuredItems
def test_updateQuality(conjured_sword):
    test_sell_in = 18
    test_quality = 40

    for i in range(0, 20):
        if test_sell_in < 0:
            test_quality -= 4

        elif test_sell_in >= 0:
            test_quality -= 2

        if test_quality <= 0:
            test_quality = 0

        conjured_sword.updateQuality()
        test_sell_in -= 1

        assert conjured_sword.quality == test_quality
        assert conjured_sword.sell_in == test_sell_in
