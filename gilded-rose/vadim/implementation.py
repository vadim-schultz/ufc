class SellIn:
    def __init__(self, days: int, step: int = 0):
        self.days = days
        self._step = step

    @property
    def expired(self):
        return self.days < 0

    def update(self):
        self.days += self._step


class Quality:
    MAX_VALUE = 50
    MIN_VALUE = 0
    def __init__(self, value: int, step: int = 0):
        self._value = self._constrain(value)
        self._step = step

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = self._constrain(value)

    def update(self):
        self.value += self._step

    def _constrain(self, value):
        return max(self.MIN_VALUE, min(value, self.MAX_VALUE))


class Strategy:
    def __init__(self, sell_in: int, quality: int):
        self._sell_in = SellIn(sell_in)
        self._quality = Quality(quality)

    @property
    def sell_in(self):
        return self._sell_in.days

    @property
    def quality(self):
        return self._quality.value

    def update(self):
        self._quality.update()
        self._sell_in.update()


class DepreciatingStrategy(Strategy):
    def __init__(self, sell_in: int, quality: int):
        self._sell_in = SellIn(sell_in, step=-1)
        self._quality = Quality(quality, step=self._get_step())

    @property
    def quality(self):
        self._quality = Quality(self._quality.value, step=self._get_step())
        return self._quality.value

    def _get_step(self):
        if self._sell_in.expired:
            return -2
        return -1


class AcceleratedDepreciatingStrategy(Strategy):
    def __init__(self, sell_in: int, quality: int):
        self._sell_in = SellIn(sell_in, step=-1)
        self._quality = Quality(quality, step=-2)


class AppreciatingStrategy(Strategy):
    def __init__(self, sell_in: int, quality: int):
        self._sell_in = SellIn(sell_in, step=-1)
        self._quality = Quality(quality, step=1)


class RiseAndCrashStrategy(Strategy):
    """
    “Backstage passes”, like aged brie, increases in Quality as it’s SellIn value approaches; Quality increases by 2
    when there are 10 days or less and by 3 when there are 5 days or less but Quality drops to 0 after the concert
    """
    def __init__(self, sell_in: int, quality: int):
        self._sell_in = SellIn(sell_in, step=-1)
        self._quality = self._get_quality(quality)

    @property
    def quality(self):
        self._quality = self._get_quality(self._quality.value)
        return self._quality.value

    def _get_step(self):
        if self._sell_in.days <= 5:
            return 3
        if self._sell_in.days <= 10:
            return 2
        return 1

    def _get_quality(self, quality):
        if self._sell_in.expired:
            return Quality(value=0)
        return Quality(value=quality, step=self._get_step())

class Item:
    def __init__(self, name: str, sell_in: int, quality: int, strategy: type[Strategy] = Strategy):
        self.name = name
        self._sell_in = sell_in
        self._quality = quality
        self._strategy = strategy(sell_in=sell_in, quality=quality)

    def __repr__(self):
        return f"Name: {self.name}, sell in: {self.sell_in}, quality: {self.quality}"

    @property
    def sell_in(self):
        return self._strategy.sell_in

    @property
    def quality(self):
        return self._strategy.quality

    def update(self):
        self._strategy.update()


class GildedRose:
    def __init__(self, items: list[Item]):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update()
