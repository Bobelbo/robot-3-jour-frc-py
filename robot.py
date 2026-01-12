import wpilib

from commands import CommandInterface
from config import config
from subsystems.remote import RemoteControllerSS


class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self._controller = RemoteControllerSS(config.get("controller"))
        self._commands: list[CommandInterface] = config["commands"]

        for command in self._commands:
            command.bind(self._controller)

    def teleopPeriodic(self):
        self._controller.update()
        self._controller.execute()
        
        for command in self._commands:
            command.update()