from typing import Any, Union

from ntcore import BooleanPublisher, DoublePublisher, IntegerPublisher, StringPublisher

GPublisher = Union[DoublePublisher, StringPublisher, BooleanPublisher, IntegerPublisher]


class GenericPublisher:
    def __init__(self, publisher: GPublisher):
        self._publisher = publisher

    def set(self, value: Any, time: int = 0):
        self._publisher.set(value)
