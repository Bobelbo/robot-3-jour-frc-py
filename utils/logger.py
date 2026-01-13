"""
Network Tables interface
"""

from ntcore import NetworkTableInstance

from utils.genericPublisher import GenericPublisher

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

    def getPublisher(self, name: str, var_type: type) -> GenericPublisher:
        publisher = self._smartDashboard.getStringTopic(name).publish()
        return publisher


Logger = _Logger()
