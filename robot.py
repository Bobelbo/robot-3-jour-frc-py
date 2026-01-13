import wpilib

from commands import CommandInterface
from config import config
from subsystems.remote import RemoteControllerSS


"""
The Robot class 
"""

class Robot(wpilib.TimedRobot):
    """
    Entrypoint of the program
    """
    def robotInit(self):
        """
        We fetch the config here
        It is here we bind and setup the command
        """
        self._controller = RemoteControllerSS(config.get("controller"))
        self._commands: list[CommandInterface] = config["commands"]

        for command in self._commands:
            command.bind(self._controller)

    def teleopPeriodic(self):
        self._controller.update()
        self._controller.execute()
        
        for command in self._commands:
            command.update()