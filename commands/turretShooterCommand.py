from typing import TYPE_CHECKING

from commands import CommandInterface
from subsystems import CANMotorSS, Pid, TurretShooterSS

# if TYPE_CHECKING:
#     from subsystems import Pid

RPM_THRESHOLD = [3000, 3500]
RPM_TARGET = (RPM_THRESHOLD[0] + RPM_THRESHOLD[1]) / 2
FEED_MOTOR_STRENGTH = 0.4
TAG = "Turret Shooter: "


class TurretShooterCommand(CommandInterface):
    def __init__(self, button: str, feedMotor: CANMotorSS, shootMotor: CANMotorSS):
        super().__init__(button)
        self._turretSS: TurretShooterSS = TurretShooterSS(feedMotor, shootMotor)
        self._shootCommand = 0

    def update(self) -> None:
        if self._shootCommand:
            self._turretSS.update()
            self._turretSS.shoot()

    def _condition(self, btn_v, index: int) -> bool:
        return True

    def _trigger(self, btn_v, index: int) -> None:
        self._shootCommand = btn_v
        if self._shootCommand:
            self._turretSS.shoot()
        else:
            self._turretSS.stop()
