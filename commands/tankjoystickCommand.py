import wpilib
import rev

from typing import List

from commands import CommandInterface

class TankJoystickCommand(CommandInterface):
    joystick: wpilib.Joystick = None
    left_motors: List[rev.SparkMax] = []
    right_motors: List[rev.SparkMax] = []

    def __init__(self, joystick, leftMotors, rightMotors):
        self.joystick = joystick
        self.left_motors = leftMotors
        self.right_motors = rightMotors

    def _update(self) -> None:
        return super()._update()

    def _condition(self) -> bool:
        return super()._condition()

    def _execute(self) -> None:
        forward_acceleration = self.joystick.getRawAxis(1)

        for motor in self.left_motors:
            motor.set(forward_acceleration)

        for motor in self.right_motors:
            motor.set(-forward_acceleration)