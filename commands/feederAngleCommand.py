from commands import CommandInterface
from subsystems.canMotorSS import CANMotorSS


class FeederAngleCommand(CommandInterface):
    _motor: CANMotorSS

    def __init__(self, btns, motor):
        """Needs two buttons, one up and one down"""
        super().__init__(btns)
        self._motor = motor

    def _trigger(self, btn_v, index: int = 0) -> None:
        # Up = 0 down = 1
        if btn_v == 1 and index == 1:
            self._motor.set_output(0.1)
        elif btn_v == 1 and index == 0:
            self._motor.set_output(-0.1)
        else:
            self._motor.stop()
