from typing import TYPE_CHECKING

from subsystems import CANMotorSS, Pid, subsystemInterface

# if TYPE_CHECKING:
#     from subsystems import Pid

RPM_THRESHOLD = [5000, 6000]
RPM_TARGET = (RPM_THRESHOLD[0] + RPM_THRESHOLD[1]) / 2
FEED_MOTOR_STRENGTH = 0.6


class TurretShooterSS(subsystemInterface.SubsystemInterface):
    def __init__(self, feedMotor: CANMotorSS, shootMotor: CANMotorSS):
        self.feedMotor = feedMotor
        self.feedMotor.setBrakeMode(True)

        self.shootMotor = shootMotor
        self.shootMotor.setBrakeMode(False)

        shootPid = Pid(
            self.shootMotor.velocityGetter(),
            0.0008,
            0.0005,
            0,
            noReverse=True,
            tolerance=100,
        )
        self.shootMotor.set_pid(shootPid)

    def update(self) -> None:
        self.shootMotor.update()

    def shoot(self) -> None:
        self.shootMotor.set_target(RPM_TARGET)
        rpm = self.shootMotor.velocityGetter()()

        if (rpm > RPM_THRESHOLD[0]) and (rpm < RPM_THRESHOLD[1]):
            self.feedMotor.set_output(FEED_MOTOR_STRENGTH)
        else:
            self.feedMotor.stop()

    def stop(self) -> None:
        self.feedMotor.stop()
        self.shootMotor.stop()
