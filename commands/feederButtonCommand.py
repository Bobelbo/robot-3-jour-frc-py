import wpilib
import rev

from typing import List

from commands import CommandInterface

class FeederButtonCommand(CommandInterface):
    button: wpilib.Joystick = None
    motor: rev.SparkFlex = None

    def __init__(self, button, motor):
        self.button = button
        self.motor = motor

    def _update(self) -> None:
        return super()._update()

    def _condition(self) -> bool:
        return self.button.getRawAxis()

    def _execute(self) -> None:
        self.motor.set(0.4)