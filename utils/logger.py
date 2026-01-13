"""
Network Tables interface
"""

from enum import Enum

from ntcore import DoublePublisher, NetworkTableInstance, Publisher, StringPublisher


class PublisherType(Enum):
    Number = DoublePublisher
    String = StringPublisher


class PublisherInterface:
    def set(self, value, time):
        pass


class _Logger:
    def __init__(self):
        self._NetworkTable = NetworkTableInstance.getDefault()

        # Get a reference to a specific table (e.g., "SmartDashboard")
        # The table name "SmartDashboard" is a common convention
        self._smartDashboard = self._NetworkTable.getTable("SmartDashboard")

        # Get type-specific publishers and subscribers
        # Publishers send data, subscribers receive data
        # You must specify a default value when creating a subscriber
        # This default value is returned if the topic hasn't been published yet

    def getPublisher(self, name: str, type: PublisherType) -> PublisherInterface:
        match type:
            case PublisherType.Number:
                publisher = self._smartDashboard.getDoubleTopic(name).publish()
            case PublisherType.String:
                publisher = self._smartDashboard.getStringTopic(name).publish()

        return publisher


Logger = _Logger()
