import rev
import wpilib
from wpimath.controller import PIDController

from commands import CommandInterface

RPM_THRESHOLD = [3000, 3500]
RPM_TARGET = (RPM_THRESHOLD[0] + RPM_THRESHOLD[1]) / 2
SPARK_TYPE = rev.SparkMax | rev.SparkFlex
FEED_MOTOR_STRENGTH = 0.4


class TurretShooter(CommandInterface):
    def __init__(
        self, joystick: wpilib.Joystick, feedMotor: SPARK_TYPE, shootMotor: SPARK_TYPE
    ):
        self.joystick = joystick
        self.feedMotor = feedMotor
        feedMotorConfig = rev.SparkMaxConfig()
        feedMotorConfig.setIdleMode(rev.SparkBaseConfig.IdleMode.kBrake)
        self.feedMotor.configure(
            feedMotorConfig,
            rev.ResetMode.kResetSafeParameters,
            rev.PersistMode.kPersistParameters,
        )
        self.shootMotor = shootMotor
        shootMotorConfig = rev.SparkMaxConfig()
        shootMotorConfig.setIdleMode(rev.SparkBaseConfig.IdleMode.kCoast)
        self.shootMotor.configure(
            shootMotorConfig,
            rev.ResetMode.kResetSafeParameters,
            rev.PersistMode.kPersistParameters,
        )
        self.encoder = self.shootMotor.getEncoder()
        self.rpm: float = 0
        self.kP: float = 0.1
        self.kI: float = 0.001
        self.kD: float = 0.0
        self.pid = PIDController(self.kP, self.kI, self.kD)
        self.pid.setTolerance(100.0)

    def _update(self) -> None:
        self.rpm = self.encoder.getVelocity()

    def _condition(self) -> bool:
        return True

    def _trigger(self) -> None:
        shootCommand: bool = self.joystick.getRawButton(0)

        self._spinUp(shootCommand)

        self._shoot(self._isSpunUp())

    def _spinUp(self, hasToSpinUp: bool) -> None:
        pidOutput = self.pid.calculate(self.rpm, RPM_TARGET)

        # bang bang principle so the shooter just coasts down in speed instead of trying to brake himself
        output = pidOutput if pidOutput > 0 else 0

        self.shootMotor.set(output * hasToSpinUp)

    def _isSpunUp(self) -> bool:
        if (self.rpm > RPM_THRESHOLD[0]) and (self.rpm < RPM_THRESHOLD[1]):
            return True

        return False

    def _shoot(self, hasToShoot: bool) -> None:
        self.feedMotor.set(FEED_MOTOR_STRENGTH * hasToShoot)
