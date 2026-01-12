from commands import CommandInterface
from subsystems import CANMotorSS, Dio

TAG = "FEEDER ANGLE:"


class FeederAngleCommand(CommandInterface):
    _motor: CANMotorSS

    def __init__(self, btns: list[str], motor: CANMotorSS, dio: Dio):
        """Needs two buttons, one up and one down"""
        super().__init__(btns)
        self._motor = motor
        self._ref = 0
        self._isHomed: bool = False
        self._switch = dio
        print(f"{TAG} Initialized")

    def _update(self, btn_v, index: int) -> None:
        if not self._isHomed:
            self._homing()
        else:
            self._motor.update()

    def _trigger(self, btn_v, index: int = 0) -> None:
        print(f"{TAG} dio state: {self._switch.isTriggered()}")
        # Up = 0 down = 1
        if btn_v == 1:
            if index == 0:
                self._goUp()
            elif index == 1:
                self._goDown()
        else:
            self._motor.stop()

    def _goUp(self, mult: float = 1.0):
        self._motor.set_output(-0.2 * mult)

    def _goDown(self, mult: float = 1.0):
        if not self._switch.isTriggered():
            self._motor.set_output(0.1 * mult)

    def _homing(self):
        if self._switch.isTriggered():
            self._motor.stop()
            self._motor.resetEncoder()
            self._isHomed = True
