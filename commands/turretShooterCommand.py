from time import time

from commands import CommandInterface
from subsystems import CANMotorSS, TurretShooterSS
from utils import Logger, GenericPublisher

TAG = "Turret Shooter: "


class TurretShooterCommand(CommandInterface):
    def __init__(
        self, button: str, feedMotors: list[CANMotorSS], shootMotor: CANMotorSS
    ):
        super().__init__(button)
        self._turretSS: TurretShooterSS = TurretShooterSS(feedMotors, shootMotor)
        self._shootCommand = 0
        self._speedPublisher: GenericPublisher = Logger.getPublisher(
            "turret shooting speed", 0.0
        )
        self._lastPublish = time()

    def update(self) -> None:
        if self._shootCommand:
            self._turretSS.update()
            self._turretSS.shoot()

            if (self._lastPublish - time()) > 0.5:
                self._speedPublisher.set(self._turretSS.getShootSpeed(), 0)

    def _trigger(self, btn_v, index: int) -> None:
        self._shootCommand = btn_v
        if self._shootCommand:
            self._turretSS.shoot()
        else:
            self._turretSS.stop()
