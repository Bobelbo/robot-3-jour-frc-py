import wpilib

from config import config
from commands import CommandInterface
from subsystems.remote import RemoteControllerSS

class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self._controller = RemoteControllerSS()    

        command: CommandInterface
        for command in config['commands']: 
            command.bind()        


    def teleopPeriodic(self):
        RemoteControllerSS().update()
        RemoteControllerSS().execute()