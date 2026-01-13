from time import time

from commands import CommandInterface
from subsystems import CANMotorSS, TurretShooterSS
from utils import GenericPublisher, Logger

TAG = "Turret Shooter: "


class TurretShooterCommand(CommandInterface):
    """
    Command to control the shooting sequence
    button: shoot trigger (hold)
    feedMotors: [gateMotor, preShootMotor, slapMotor]
    shootMotor: Shoots the ball
    """

    def __init__(
        self, button: str, feedMotors: list[CANMotorSS], shootMotor: CANMotorSS
    ):
        super().__init__(button)
        self._turretSS: TurretShooterSS = TurretShooterSS(feedMotors, shootMotor)
        self._shootCommand = 0
        self._speedPublisher: GenericPublisher = Logger.getPublisher(
            "turret shooting speed", float
        )
        self._lastPublish = time()

    def update(self) -> None:
        """
        update the turret and shoot if possible if the trigger is pressed
        publish the speed on the network table
        """
        if self._shootCommand:
            self._turretSS.update()
            self._turretSS.shoot()

            if (self._lastPublish - time()) > 0.5:
                print(f"{TAG} updated speed on NT")
                self._speedPublisher.set(self._turretSS.getShootSpeed(), 0)

    def _trigger(self, btn_v, index: int) -> None:
        """
        if the button is pressed, shoot
        change the state (_shootCommand) to the state of the button
        """
        self._shootCommand = btn_v
        if self._shootCommand:
            self._turretSS.shoot()
        else:
            self._turretSS.stop()
