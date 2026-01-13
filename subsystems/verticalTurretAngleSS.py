from typing import TYPE_CHECKING, Optional

from subsystems import Pid

from .subsystemInterface import SubsystemInterface

if TYPE_CHECKING:
    from subsystems import CANMotorSS, DigitalIO

MAX_POSITION = 100

class VerticalTurretAngleSS(SubsystemInterface):

    def __init__(self, motor: "CANMotorSS", switch: "DigitalIO"):
        self._motor = motor
        self._switch = switch

        self._motor.setInverted(False)
        self._motor.setBrakeMode(True)

        # Used to find deployed solution encoder state
        self._zero: Optional[float] = None

    def update(self):
        if self._switch.isTriggered():
            self._motor.stop()

        if self._switch.isTriggered() and self._zero is None:
            self._motor.resetEncoder()

    def home(self):
        self._motor.set_output(-0.1)

    def isHomed(self):
        return self._zero is not None

    def move(self, value: float):
        if value > 0 and self._motor.get_position() < MAX_POSITION:
            self._motor.set_output(value)

        elif value < 0 and not self._switch.isTriggered():
            self._motor.set_output(value)

    def stop(self):
        self._motor.stop()
