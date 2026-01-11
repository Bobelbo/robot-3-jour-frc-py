import rev
import wpilib

from commands import CommandInterface


class FeederButtonCommand(CommandInterface):
    button: wpilib.Joystick
    motor: rev.SparkFlex

    def __init__(self, joystick, motor):
        self.joystick = joystick
        self.motor = motor

    def _update(self) -> None:
        return super()._update()

    def _condition(self) -> bool:
        return super()._condition()

    def _execute(self) -> None:
        button = self.joystick.getRawButton(1)
        self.motor.set(0.4 * button)
