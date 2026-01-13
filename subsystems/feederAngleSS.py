from typing import TYPE_CHECKING, Optional

from .subsystemInterface import SubsystemInterface

if TYPE_CHECKING:
    from subsystems import CANMotorSS, DigitalIO, Pid



class FeederAngleSS(SubsystemInterface):
    def __init__(self, motor: CANMotorSS, switch: DigitalIO):
        self._motor = motor
        self._switch = switch

        self._motor.setInverted(False)
        self._motor.setBrakeMode(True)
        self._motor.set_pid(Pid(
            self._motor.positionGetter(),
            kp=0.0001,
            ki=0.0000001,
            kd=0,
        ))

        # Used to find deployed solution encoder state
        self._zero: Optional[float] = None
        self._holding = False

    def update(self):
        if self._holding:
            self._motor.update()

        if self._switch.isTriggered():
            self._motor.stop()
            self._zero = self._motor.encoder.getPosition()

    def findHome(self): 
        self._holding = False
        if self._zero is None:
            self._motor.set_output(0.1)
        else:
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