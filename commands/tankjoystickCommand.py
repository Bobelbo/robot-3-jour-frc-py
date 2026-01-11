from typing import List

import rev
import wpilib

from .commandInterface import CommandInterface


class TankJoystickCommand(CommandInterface):
    """Tank drive control using a joystick."""

    joystick: wpilib.Joystick
    left_motors: List[rev.SparkMax] = []
    right_motors: List[rev.SparkMax] = []

    axis_deadzone: float = 0.1

    def __init__(self, joystick, leftMotors, rightMotors):
        self.joystick = joystick
        self.left_motors = leftMotors
        self.right_motors = rightMotors

    def _update(self) -> None:
        pass

    def _condition(self) -> bool:
        return True

    def _trigger(self) -> None:
        smoothing_gradient = -self.joystick.getRawAxis(2)

        side_rotation = self.joystick.getRawAxis(0)
        forward_acceleration = self.joystick.getRawAxis(1)

        # if value delta is smaller than 0.1, set to 0
        if abs(side_rotation) < 0.1:
            side_rotation = 0.0
        if abs(forward_acceleration) < 0.1:
            forward_acceleration = 0.0

        forward_acceleration *= 1.0 - smoothing_gradient
        side_rotation *= 1.0 - smoothing_gradient

        for motor in self.left_motors:
            motor.set(-forward_acceleration)

        for motor in self.right_motors:
            motor.set(forward_acceleration)
