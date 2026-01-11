import rev

from typing import List

from .subsystemInterface import SubsystemInterface

class CANMotorSS(SubsystemInterface):
    """SubSystem for controlling a brushless sparkMax motor controller over CAN bus."""
    _motor = None

    def __init__(self, can_id: int):
        super().__init__()
        self._motor = rev.SparkMax(can_id, rev.SparkLowLevel.MotorType.kBrushless)

    def set_speed(self, speed: float) -> None:
        """Set the speed of the motor."""
        self._motor.set(speed)

    def stop(self) -> None:
        """Stop motor."""
        self._motor.set(0.0)