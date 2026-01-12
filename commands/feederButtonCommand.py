from commands import CommandInterface
from subsystems.canMotorSS import CANMotorSS


class FeederButtonCommand(CommandInterface):
    _motor: CANMotorSS
    _state_on: bool

    def __init__(self, btn_id: str, motor: CANMotorSS):
        super().__init__(btn_id)
        self.motor = motor
        self._state_on = False

    def _trigger(self, btn_v: bool) -> None:
        self.motor.set_speed(0.4 * btn_v)
