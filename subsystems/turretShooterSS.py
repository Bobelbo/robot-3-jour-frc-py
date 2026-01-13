from subsystems import CANMotorSS, Pid, subsystemInterface

RPM_THRESHOLD = [5000, 6000]
RPM_TARGET = (RPM_THRESHOLD[0] + RPM_THRESHOLD[1]) / 2
FEED_MOTOR_STRENGTH = 0.6


class TurretShooterSS(subsystemInterface.SubsystemInterface):
    def __init__(self, feedMotors: list[CANMotorSS], shootMotor: CANMotorSS):
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
        self._shootMotor.update()

    def shoot(self) -> None:
        self._shootMotor.set_target(RPM_TARGET)
        rpm = self._shootMotor.velocityFunctionGetter()()

        if (rpm > RPM_THRESHOLD[0]) and (rpm < RPM_THRESHOLD[1]):
            for motor in self._feedMotors:
                motor.set_output(FEED_MOTOR_STRENGTH)
        else:
            for motor in self._feedMotors:
                motor.stop()

    def stop(self) -> None:
        for motor in self._feedMotors:
            motor.stop()
        self._shootMotor.stop()

    def getShootSpeed(self) -> float:
        return self._shootMotor.velocityFunctionGetter()()
