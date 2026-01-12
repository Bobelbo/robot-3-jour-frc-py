from typing import TYPE_CHECKING

from subsystems import CANMotorSS, Pid, subsystemInterface

# if TYPE_CHECKING:
#     from subsystems import Pid

RPM_THRESHOLD = [3000, 3500]
RPM_TARGET = (RPM_THRESHOLD[0] + RPM_THRESHOLD[1]) / 2
FEED_MOTOR_STRENGTH = 0.4


class TurretShooterSS(subsystemInterface.SubsystemInterface):
    def __init__(self, feedMotor: CANMotorSS, shootMotor: CANMotorSS):
        self.feedMotor = feedMotor
        self.feedMotor.setBrakeMode(True)

        self.shootMotor = shootMotor
        self.shootMotor.setBrakeMode(False)

        shootPid = Pid(
            self.shootMotor.velocityGetter(),
            0.1,
            0.0001,
            0,
            noReverse=True,
            tolerance=100,
        )
        self.shootMotor.set_pid(shootPid)

    def _update(self, btn_v, index: int) -> None:
        self.shootMotor.update()

    def shoot(self) -> None:
        self.shootMotor.set_speed(RPM_TARGET)
        rpm = self.shootMotor.velocityGetter()()

        if (rpm > RPM_THRESHOLD[0]) and (rpm < RPM_THRESHOLD[1]):
            self.feedMotor.set_output(FEED_MOTOR_STRENGTH)
        else:
            self.feedMotor.stop()

    def stop(self) -> None:
        self.feedMotor.stop()
        self.shootMotor.stop()
