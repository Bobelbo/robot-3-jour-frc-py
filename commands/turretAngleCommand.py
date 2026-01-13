from commands import CommandInterface
from subsystems import CANMotorSS, DigitalIO
from subsystems.verticalTurretAngleSS import VerticalTurretAngleSS

DEADZONE = 0.2
TAG = "Turret Angle:"


class TurretAngleCommand(CommandInterface):
    _max_turret_rotation = 87
    _max_turret_angle = 10

    def __init__(self, btn_id: list[str], horizontal_motor: CANMotorSS, vertical_motor: CANMotorSS, vertical_switch: DigitalIO):
        """Can have up to 3 inputs, Horizontal, Vertical axies and toggle input"""
        super().__init__(btn_id)

        self._horizontal_motor = horizontal_motor
        self._vertical_drive = VerticalTurretAngleSS(vertical_motor, vertical_switch)

        self._horizontal_motor.setBrakeMode(True)

        self._on = False

    def update(self):
        self._vertical_drive.update()

    def _update(self, btn_v, index):
        if index == 2 and btn_v == 1:
            self._on = not self._on

    def _condition(self, btn_v, index):
        return self._on

    def _trigger(self, btn_v, index) -> None:
        if index == 0 and abs(btn_v):
            self._horizontal_move(btn_v)
        if index == 1 and abs(btn_v):
            self._vertical_move(btn_v)

    def _horizontal_move(self, value: float):
        inputTransform: float = 0.1
        if abs(value) < DEADZONE:
            self._horizontal_motor.stop()
            return
        value = value * inputTransform

        self._horizontal_motor.set_output(value)

    def _vertical_move(self, value: float):
        inputTransform: float = 0.1
        if abs(value) < DEADZONE:
            # print(f"{TAG} horizontal DEADZONE reached")
            self._vertical_drive.stop()
            return
        # print(f"{TAG} horizontal command: {command}")

        self._vertical_drive.move(value)
