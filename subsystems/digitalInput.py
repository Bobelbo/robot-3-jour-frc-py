from wpilib import DigitalInput

from .subsystemInterface import SubsystemInterface


class Dio(SubsystemInterface):
    def __init__(self, port: int):
        self._port = float
        self._dio = DigitalInput(port)

    def setTarget(self, target: float) -> None:
        self.pidTarget = target

    def isTriggered(self) -> float:
        # its a pull-up
        return not self._dio.get()
