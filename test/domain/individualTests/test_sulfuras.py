from domain.items.sulfuras import Sulfuras
import pytest


@pytest.fixture
def sulfur():
    test_sulfuras = Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)

    return test_sulfuras


@pytest.mark.sulfuras
def test_updateQuality(sulfur):
    for i in range(0, 15):
        sulfur.updateQuality()

        assert sulfur.sell_in == -1
        assert sulfur.quality == 80
