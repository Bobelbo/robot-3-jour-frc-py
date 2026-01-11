import wpilib
from typing import List

from commands.commandInterface import CommandInterface

class tankjoystickCommand(CommandInterface):
    joystick: wpilib.Joystick = None
    left_motors: List[wpilib.SparkMax] = []
    right_motors: List[wpilib.SparkMax] = []

    def __init__(self, joystick, leftMotors, rightMotors):
        self.joystick = joystick
        self.left_motors = leftMotors
        self.right_motors = rightMotors

    def execute(self) -> None:
        forward_acceleration = self.joystick.getRawAxis(1)

        for motor in self.left_motors:
            motor.set(forward_acceleration)

        for motor in self.right_motors:
            motor.set(-forward_acceleration)