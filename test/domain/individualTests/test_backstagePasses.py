from domain.items.backstage import Backstage
import pytest


@pytest.fixture
def backstage_pass():
    test_backstage_pass = Backstage("Backstage passes to a TAFKAL80ETC concert", 15, 20)

    return test_backstage_pass


@pytest.mark.backstagePasses
def test_updateQuality(backstage_pass):
    test_sell_in = 15
    test_quality = 20

    for i in range(0, 20):
        if test_sell_in > 10:
            test_quality += 1

        elif 5 < test_sell_in <= 10:
            test_quality += 2

        elif 0 < test_sell_in <= 5:
            test_quality += 3

        elif test_sell_in <= 0:
            test_quality = 0

        if test_quality >= 50:
            test_quality = 50

        backstage_pass.updateQuality()
        test_sell_in -= 1

        assert test_quality == backstage_pass.quality
        assert test_sell_in == backstage_pass.sell_in
