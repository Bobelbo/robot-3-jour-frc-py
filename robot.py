import wpilib

from config import config
from commands import CommandInterface
from subsystems.remote import RemoteControllerSS

class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self._controller = RemoteControllerSS(config.get('controller'))    

        command: CommandInterface
        for command in config['commands']: 
            command.bind(self._controller)        


    def teleopPeriodic(self):
        self._controller.update()
        self._controller.execute()