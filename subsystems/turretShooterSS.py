from typing import TYPE_CHECKING
from subsystems import Pid, subsystemInterface

if TYPE_CHECKING:
    from subsystems import CANMotorSS

RPM_THRESHOLD = [3300, 4300]
RPM_TARGET = (RPM_THRESHOLD[0] + RPM_THRESHOLD[1]) / 2
FEED_MOTOR_STRENGTH = [0.5, -1, -0.8]


class TurretShooterSS(subsystemInterface.SubsystemInterface):
    """
    Turret shooter subsystem
    feedMotors: [gateMotor, preShootMotor, slapMotor]
    shootMotor: Shoots the ball
    """

    def __init__(self, feedMotors: list['CANMotorSS'], shootMotor: 'CANMotorSS'):
        self._feedMotors = feedMotors
        for motor in self._feedMotors:
            motor.setBrakeMode(True)

        self._shootMotor = shootMotor
        self._shootMotor.setBrakeMode(False)

        shootPid = Pid(
            self._shootMotor.velocityFunctionGetter(),
            0.0008,
            0.0005,
            0,
            noReverse=True,
            tolerance=100,
        )
        self._shootMotor.set_pid(shootPid)

    def update(self) -> None:
        """
        updates the motors
        """
        self._shootMotor.update()

    def shoot(self) -> None:
        """
        Spin up the shooter and shoots if the speed is in the RPM_THRESHOLD
        """
        self._shootMotor.set_target(RPM_TARGET)
        rpm = self._shootMotor.velocityFunctionGetter()()

        if (rpm > RPM_THRESHOLD[0]) and (rpm < RPM_THRESHOLD[1]):
            for motor, speed in zip(self._feedMotors, FEED_MOTOR_STRENGTH):
                motor.set_output(speed)
        else:
            for motor in self._feedMotors:
                motor.stop()

    def stop(self) -> None:
        """
        stops all the motors
        """
        for motor in self._feedMotors:
            motor.stop()
        self._shootMotor.stop()

    def getShootSpeed(self) -> float:
        """
        returns the shooting motor's velocity
        """
        return self._shootMotor.velocityFunctionGetter()()
