from typing import Protocol, List, Dict

MAX_QUALITY = 50
MIN_QUALITY = 0


class QualityStrategy(Protocol):
    def update_quality(self, item: "Item") -> None:
        """Update the quality and sell_in of the item."""
        ...


class NormalItemStrategy:
    def update_quality(self, item: "Item") -> None:
        item.sell_in -= 1
        item.quality = max(MIN_QUALITY, item.quality - 1)

        if item.sell_in < 0:
            item.quality = max(MIN_QUALITY, item.quality - 1)


class AgedBrieStrategy:
    def update_quality(self, item: "Item") -> None:
        item.sell_in -= 1
        item.quality = min(MAX_QUALITY, item.quality + 1)

        if item.sell_in < 0:
            item.quality = min(MAX_QUALITY, item.quality + 1)


class SulfurasStrategy:
    def update_quality(self, item: "Item") -> None:
        pass


class BackstagePassStrategy:
    def update_quality(self, item: "Item") -> None:
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = MIN_QUALITY
        elif item.sell_in < 5:
            item.quality = min(MAX_QUALITY, item.quality + 3)
        elif item.sell_in < 10:
            item.quality = min(MAX_QUALITY, item.quality + 2)
        else:
            item.quality = min(MAX_QUALITY, item.quality + 1)


class ConjuredItemStrategy:
    def update_quality(self, item: "Item") -> None:
        item.sell_in -= 1
        decrement = 2 if item.sell_in >= 0 else 4
        item.quality = max(MIN_QUALITY, item.quality - decrement)


class Item:
    def __init__(self, name: str, sell_in: int, quality: int, strategy: QualityStrategy):
        self.name = name
        self.sell_in = sell_in
        self.quality = min(MAX_QUALITY, quality)
        self.strategy = strategy

    def update_quality(self) -> None:
        self.strategy.update_quality(self)

    def __repr__(self) -> str:
        return f"{self.name}, SellIn: {self.sell_in}, Quality: {self.quality}"


class ItemFactory:
    strategy_map: Dict[str, QualityStrategy] = {
        "Aged Brie": AgedBrieStrategy(),
        "Sulfuras": SulfurasStrategy(),
        "Backstage Pass": BackstagePassStrategy(),
        "Conjured": ConjuredItemStrategy(),
    }

    @staticmethod
    def create_item(name: str, sell_in: int, quality: int) -> Item:
        strategy = ItemFactory.strategy_map.get(name, NormalItemStrategy())
        return Item(name, sell_in, quality, strategy)


class GildedRose:
    def __init__(self, items: List[Item]):
        self.items = items

    def update_items(self) -> None:
        for item_ in self.items:
            item_.update_quality()
