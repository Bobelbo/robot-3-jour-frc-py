from typing import TypeVar, type

from ntcore import NetworkTable

from .genericPublisher import GenericPublisher

T = TypeVar("T")

class SmartDashboardManager():
    def __init__(self, table: NetworkTable ):
        self._table = table

    def getPublisher(self, name: str, var_type: type) -> GenericPublisher[T]:
        publisher = None

        match var_type:
            case float():
                publisher = self._table.getDoubleTopic(name).publish()
            case str():
                publisher = self._table.getStringTopic(name).publish()
            case bool():
                publisher = self._table.getBooleanTopic(name).publish()
            case int():
                publisher = self._table.getIntegerTopic(name).publish()
            case _:
                raise NotImplementedError(f"Type: {type(var_type)} not supported for logging")

        return GenericPublisher(publisher)[var_type]