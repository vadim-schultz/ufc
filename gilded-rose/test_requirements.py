import pytest

from gilded_rose import ItemFactory, GildedRose


@pytest.fixture
def sut():
    items = [
        ItemFactory.create_item("Normal Item", 10, 20),
        ItemFactory.create_item("Aged Brie", 2, 0),
        ItemFactory.create_item("Sulfuras", 0, 80),
        ItemFactory.create_item("Backstage Pass", 15, 20),
        ItemFactory.create_item("Conjured", 3, 6),
    ]

    return GildedRose(items)


def test_normal_item_quality_decreases():
    normal_item = ItemFactory.create_item("Normal Item", 10, 20)
    old_quality = normal_item.quality
    normal_item.update_quality()
    assert normal_item.quality <= old_quality


def test_quality_is_never_negative(sut):
    highest_sellin = max(sut.items, key=lambda item: item.sell_in).sell_in
    [sut.update_items() for _ in range(highest_sellin + 1)]
    assert min(sut.items, key=lambda item: item.quality).quality >= 0


def test_quality_is_never_more_then_50():
    item = ItemFactory.create_item("Aged Brie", 0, 80)
    item.update_quality()
    assert item.quality == 50


def test_after_sell_date_normal_item_quality_decreases_twice_as_fast():
    item = ItemFactory.create_item("Normal Item", 5, origin_quality := 50)
    [item.update_quality() for _ in range(5)]
    quality_div_before_sellin = origin_quality - item.quality
    [item.update_quality() for _ in range(5)]
    quality_div_after_sellin = origin_quality - quality_div_before_sellin - item.quality
    assert quality_div_before_sellin * 2 == quality_div_after_sellin


def test_quality_of_sulfuras_is_constant(sut):
    [sut.update_items() for _ in range(100)]
    assert next((obj for obj in sut.items if obj.name == "Sulfuras")).quality == 50


def test_aged_brie_quality_never_decreases():
    aged_brie = ItemFactory.create_item("Aged Brie", 2, 0)
    old_quality = aged_brie.quality
    for i in range(1000):
        aged_brie.update_quality()
        assert aged_brie.quality >= old_quality
        old_quality = aged_brie.quality
    assert aged_brie.quality == 50


def test_backstage_pass_quality_increases():
    item = ItemFactory.create_item("Backstage Pass", 15, 20)
    item.update_quality()
    assert item.quality == 21


def test_backstage_pass_quality_increases_faster_when_close():
    item = ItemFactory.create_item("Backstage Pass", 10, 20)
    item.update_quality()
    assert item.quality == 22


def test_backstage_pass_quality_drops_to_zero_after_concert():
    item = ItemFactory.create_item("Backstage Pass", 0, 20)
    item.update_quality()
    assert item.quality == 0


def test_conjured_item_quality_decreases_twice_as_fast():
    item = ItemFactory.create_item("Conjured", 10, 20)
    item.update_quality()
    assert item.quality == 18
