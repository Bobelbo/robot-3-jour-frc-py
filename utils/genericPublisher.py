from typing import Generic, TypeVar, Union

from ntcore import DoublePublisher, StringPublisher, BooleanPublisher, IntegerPublisher

GPublisher = Union[DoublePublisher, StringPublisher, BooleanPublisher, IntegerPublisher]

T = TypeVar("T")

class GenericPublisher(Generic[T]):
    def __init__(self, publisher: GPublisher):
        self._publisher = publisher
    
    def set(self, value: T, time: int = 0) -> T:
        self._publisher.set(value)