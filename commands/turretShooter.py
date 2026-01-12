from commands import CommandInterface
from subsystems.canMotorSS import CANMotorSS
from subsystems.pid import Pid

RPM_THRESHOLD = [3000, 3500]
RPM_TARGET = (RPM_THRESHOLD[0] + RPM_THRESHOLD[1]) / 2
FEED_MOTOR_STRENGTH = 0.4


class TurretShooterCommand(CommandInterface):
    def __init__(self, button: str, feedMotor: CANMotorSS, shootMotor: CANMotorSS):
        super().__init__(button)
        self.feedMotor = feedMotor
        self.feedMotor.setBrakeMode(True)

        self.shootMotor = shootMotor
        self.shootMotor.setBrakeMode(False)

        shootPid = Pid(
            self.shootMotor.getEncoder().getVelocity,
            0.1,
            0.0001,
            0,
            noReverse=True,
            tolerance=100,
        )
        self.shootMotor.set_pid(shootPid)

    def _update(self, btn_v) -> None:
        self.shootMotor.update()

    def _condition(self, btn_v) -> bool:
        return True

    def _trigger(self, btn_v) -> None:
        shootCommand: bool = btn_v

        if shootCommand:
            self.shootMotor.set_speed(RPM_TARGET)
            self._shoot()
        else:
            self.shootMotor.stop()
            self.feedMotor.stop()

    def _shoot(self) -> None:
        rpm = self.shootMotor.getEncoder().getVelocity()

        if (rpm > RPM_THRESHOLD[0]) and (rpm < RPM_THRESHOLD[1]):
            self.feedMotor.set_output(FEED_MOTOR_STRENGTH)
        else:
            self.feedMotor.stop()
