from commands import CommandInterface
from subsystems import CANMotorSS, DigitalIO, FeederAngleSS

TAG = "FEEDER ANGLE:"


class FeederAngleCommand(CommandInterface):
    _motor: CANMotorSS

    def __init__(
        self, btns: list[str], motor: CANMotorSS, deployed_limit_switch: DigitalIO
    ):
        """Needs two buttons, one up and one down"""
        super().__init__(btns)
        self._feeder_subsystem = FeederAngleSS(motor, deployed_limit_switch)
        print(f"{TAG} Initialized")

    def update(self) -> None:
        self._feeder_subsystem.update()

        if not self._feeder_subsystem.isHomed():
            self._feeder_subsystem.home()

    def _trigger(self, btn_v, index: int = 0) -> None:
        # Up = 0 down = 1
        if index == 0:
            self.upBtn(btn_v)
        elif index == 1:
            self.downBtn(btn_v)

    def upBtn(self, value):
        """Will be used to raise and hold the ramp"""
        if value == 0:
            self._feeder_subsystem.stop()
        else:
            self._feeder_subsystem.up()

    def downBtn(self, value):
        """If we click the down button it is because we want the feeder to the floor"""
        if value == 1:
            self._feeder_subsystem.down()
