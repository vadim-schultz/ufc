import pytest

from .implementation import (
    Item,
    DepreciatingStrategy,
    AppreciatingStrategy,
    AcceleratedDepreciatingStrategy,
    RiseAndCrashStrategy
)


def test_normal_depreciation():
    """At the end of each day our system lowers both values for every item."""
    item = Item(name="Elixir of the Mongoose", sell_in=10, quality=10, strategy=DepreciatingStrategy)
    item.update()
    assert item.quality == 9
    assert item.sell_in == 9


def test_max_quality():
    """The Quality of an item is never more than 50."""
    item = Item(name="Aged Brie", sell_in=1, quality=50, strategy=AppreciatingStrategy)
    item.update()
    assert item.quality == 50


def test_above_max_quality():
    """The Quality of an item is never more than 50."""
    item = Item(name="Special price", sell_in=1, quality=80)
    assert item.quality == 50


def test_min_quality():
    """The Quality of an item is never negative."""
    item = Item(name="Elixir of the Mongoose", sell_in=1, quality=0, strategy=DepreciatingStrategy)
    assert item.quality == 0


def test_below_min_quality():
    """The Quality of an item is never negative."""
    item = Item(name="Only for you", sell_in=1, quality=-1)
    assert item.quality == 0


def test_quality_degrades_2x_after_sellby():
    """Once the sell by date has passed, Quality degrades twice as fast."""
    item = Item(name="Elixir of the Mongoose", sell_in=0, quality=10,
                strategy=DepreciatingStrategy)  # depreciates in quality
    item.update()
    assert item.quality == 9
    item.update()
    assert item.quality == 7


def test_quality_degrades_2x_negative_sellby():
    """Once the sell by date has passed, Quality degrades twice as fast."""
    item = Item(name="Elixir of the Mongoose", sell_in=-1, quality=10,
                strategy=DepreciatingStrategy)  # depreciates in quality
    item.update()
    assert item.quality == 8


def test_quality_increase_aged_brie():
    """“Aged Brie” actually increases in Quality the older it gets."""
    item = Item(name="Aged Brie", sell_in=1, quality=1, strategy=AppreciatingStrategy)
    item.update()
    assert item.quality == 2


def test_sulfuras():
    """“Sulfuras”, being a legendary item, never has to be sold or decreases in Quality."""
    item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=1, quality=1)
    item.update()
    assert item.quality == 1
    assert item.sell_in == 1


@pytest.mark.parametrize("sell_in, quality, expected", [(15, 20, 21), (9, 20, 22), (4, 20, 23), (0, 20, 0)])
def test_backstage_passes(sell_in, quality, expected):
    """
    “Backstage passes”, like aged brie, increases in Quality as it’s SellIn value approaches; Quality increases by 2
    when there are 10 days or less and by 3 when there are 5 days or less but Quality drops to 0 after the concert
    """
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=sell_in, quality=quality,
                strategy=RiseAndCrashStrategy)
    item.update()
    assert item.quality == expected


def test_conjured():
    """“Conjured” items degrade in Quality twice as fast as normal items."""
    item = Item(name="Conjured Mana Cake", sell_in=3, quality=6, strategy=AcceleratedDepreciatingStrategy)
    item.update()
    assert item.quality == 4
