from typing import TYPE_CHECKING, List

from .apid import Pid
from .subsystemInterface import SubsystemInterface

if TYPE_CHECKING:
    from subsystems import CANMotorSS, Pid


class CanTankDriveSS(SubsystemInterface):
    """Subsystem for controlling a tank drive using CAN SparkMax motor controllers."""

    def __init__(
        self, left_motors: List["CANMotorSS"], right_motors: List["CANMotorSS"]
    ):
        super().__init__()
        self.left_motors = left_motors
        self.right_motors = right_motors

        self._lpid = Pid(
            dataGetter=self.left_motors[0].velocityFunctionGetter(),
            kp=0.01,
            ki=0.0001,
            tolerance=5,
            noReverse=False,
        )

        self._rpid = Pid(
            dataGetter=self.right_motors[0].velocityFunctionGetter(),
            kp=0.01,
            ki=0.0001,
            tolerance=5,
            noReverse=False,
        )

        for motor in self.left_motors:
            motor.setBrakeMode(False)
            motor.setInverted(True)
            motor.set_pid(self._lpid)
        for motor in self.right_motors:
            motor.setBrakeMode(False)
            motor.setInverted(False)
            motor.set_pid(self._rpid)

    def update(self):
        for motor in self.left_motors + self.right_motors:
            motor.update()

    def set_left_speed(self, speed: float) -> None:
        """Set the speed of the left motors."""
        if speed != 0:
            for motor in self.left_motors:
                motor.set_target(speed)
        else:
            for motor in self.left_motors:
                motor.stop()

    def set_right_speed(self, speed: float) -> None:
        """Set the speed of the right motors."""
        if speed != 0:
            for motor in self.right_motors:
                motor.set_target(speed)
        else:
            for motor in self.right_motors:
                motor.stop()

    def stop(self) -> None:
        """Stop all motors."""
        for motor in self.left_motors + self.right_motors:
            motor.stop()
