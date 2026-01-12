from commands import CommandInterface
from subsystems.canMotorSS import CANMotorSS


class FeederButtonCommand(CommandInterface):
    _motor: CANMotorSS
    _state_on: bool

    def __init__(self, btn_id: str, motor: CANMotorSS):
        super().__init__(btn_id)
        self.motor = motor
        self._state_on = False

        print("FeederButtonCommand Enabled")

    def _trigger(self, btn_v: bool, index: int = 0) -> None:
        print(f"FeederButtonCommand Trigger: v={btn_v} i={index}")
        self.motor.set_output(0.4) if btn_v else self.motor.stop()
