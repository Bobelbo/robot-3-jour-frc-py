import wpilib

from config import config

class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self.commands = config['commands']

    def teleopPeriodic(self):
        for command in self.commands:
            command.trigger()