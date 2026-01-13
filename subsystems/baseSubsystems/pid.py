from typing import Callable

from wpimath.controller import PIDController

from ..subsystemInterface import SubsystemInterface


class Pid(SubsystemInterface):
    def __init__(
        self,
        dataGetter: Callable[[], float],
        kp: float,
        ki: float,
        kd=0.0,
        tolerance=0,
        noReverse: bool = False,
    ):
        self.pidTarget: float = 0
        self.kP: float = kp
        self.kI: float = ki
        self.kD: float = kd
        self.pidNoReverse = noReverse
        self.pid = PIDController(self.kP, self.kI, self.kD)
        self.pid.setTolerance(tolerance)
        self.currentData = dataGetter
        self.output: float = 0

    def update(self) -> None:
        """updates running even if input did not change"""

        currentData = self.currentData()
        pidOutput = self.pid.calculate(currentData, self.pidTarget)

        # bang bang principle so the shooter just coasts down in speed instead of trying to brake himself
        if self.pidNoReverse:
            output = pidOutput if pidOutput > 0 else 0
        # Normal pid behavior
        else:
            output = pidOutput

        self.output = output

    def setTarget(self, target: float) -> None:
        self.pidTarget = target

    def getOutput(self) -> float:
        return self.output
