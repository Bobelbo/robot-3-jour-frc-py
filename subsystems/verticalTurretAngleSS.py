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
        if self._holding:
            self._motor.update()

        if self._switch.isTriggered():
            self._motor.stop()
            self._zero = self._motor.encoder.getPosition()

        if self._switch.isTriggered() and self._zero is None:
            self._motor.resetEncoder()

    def home(self):
        self._holding = False
        self._motor.set_output(0.1)

    def down(self):
        assert self._zero
        self._holding = False
        self._motor.set_target(self._zero)

    def isHomed(self):
        return self._zero is not None

    def up(self):
        self._holding = False
        self._motor.set_output(0.12)

    def hold(self):
        self._holding = True
        self._motor.stop()
        self._motor.set_target(self._motor.encoder.getPosition())
