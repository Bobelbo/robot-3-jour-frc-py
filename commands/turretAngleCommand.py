from commands import CommandInterface
from subsystems import CANMotorSS

DEADZONE = 0.2
TAG = "Turret Angle:"


class TurretAngleCommand(CommandInterface):
    _max_turret_rotation = 87
    _max_turret_angle = 10

    def __init__(self, btn_id: list[str], hMotor: CANMotorSS, vMotor: CANMotorSS):
        """Can have up to 3 inputs, Horizontal, Vertical axies and toggle input"""
        super().__init__(btn_id)

        self._hMotor = hMotor
        self._vMotor = vMotor

        self._hMotor.setBrakeMode(True)
        self._vMotor.setBrakeMode(True)

        self._on = False

    def _update(self, btn_v, index):
        if index == 2 and btn_v == 1:
            self._on = not self._on

    def _condition(self, btn_v, index):
        return self._on

    def _trigger(self, btn_v, index) -> None:
        if index == 0 and abs(btn_v):
            self._hMove(btn_v)
        if index == 1 and abs(btn_v):
            self._vMove(btn_v)

    def _hMove(self, command: float):
        inputTransform: float = 0.1
        if abs(command) < DEADZONE:
            self._hMotor.stop()
            return
        command = command * inputTransform

        self._hMotor.set_output(command)

    def _vMove(self, command: float):
        inputTransform: float = 0.1
        if abs(command) < DEADZONE:
            # print(f"{TAG} horizontal DEADZONE reached")
            self._vMotor.stop()
            return
        command = command * inputTransform
        # print(f"{TAG} horizontal command: {command}")

        self._vMotor.set_output(command)
