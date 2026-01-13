from commands import CommandInterface
from subsystems import CANMotorSS

TAG = "Climber:"


class ClimberCommand(CommandInterface):
    """
    Simple climber
    btns: [up, down]
    motor: winch
    """

    def __init__(self, btns: list[str], motor: CANMotorSS):
        """Needs two buttons, one up and one down"""
        super().__init__(btns)
        self._motor = motor

    def _trigger(self, btn_v, index) -> None:
        """
        up, down or stops the motor
        """
        # Up = 0 down = 1

        if btn_v == 1:
            if index == 0:
                self._goUp()
            elif index == 1:
                self._goDown()
        else:
            self._motor.stop()

    def _goUp(self, mult: float = 1.0):
        self._motor.set_output(-0.5 * mult)

    def _goDown(self, mult: float = 1.0):
        self._motor.set_output(0.5 * mult)
