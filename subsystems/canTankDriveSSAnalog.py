from typing import TYPE_CHECKING, List

from .baseSubsystems.pid import Pid
from .subsystemInterface import SubsystemInterface

if TYPE_CHECKING:
    from subsystems import CANMotorSSAnalog


class CanTankDriveSSAnalog(SubsystemInterface):
    """Subsystem for controlling a tank drive using CAN SparkMax motor controllers."""

    def __init__(
        self, left_motors: List["CANMotorSS"], right_motors: List["CANMotorSS"]
    ):
        super().__init__()
        self.left_motors = left_motors
        self.right_motors = right_motors

        for motor in self.left_motors:
            motor.setBrakeMode(False)
            motor.setInverted(False)
        for motor in self.right_motors:
            motor.setBrakeMode(False)
            motor.setInverted(True)

    def update(self):
        pass

    def set_left_speed(self, output: float) -> None:
        """Set the speed of the left motors."""
        if output != 0:
            for motor in self.left_motors:
                motor.set_output(output)
        else:
            for motor in self.left_motors:
                motor.stop()

    def set_right_speed(self, output: float) -> None:
        """Set the speed of the right motors."""
        if output != 0:
            for motor in self.right_motors:
                motor.set_output(output)
        else:
            for motor in self.right_motors:
                motor.stop()

    def stop(self) -> None:
        """Stop all motors."""
        for motor in self.left_motors + self.right_motors:
            motor.stop()
