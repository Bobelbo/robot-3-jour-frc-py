from enum import Enum
from typing import Callable

import rev

from .pid import Pid
from .subsystemInterface import SubsystemInterface

SPARK_TYPE = rev.SparkMax | rev.SparkFlex
TAG = "CANMotorSS:"


class CANMotorType(Enum):
    SPARKMAX = rev.SparkMax
    SPARKFLEX = rev.SparkFlex


class CANMotorSS(SubsystemInterface):
    """SubSystem for controlling a brushless sparkMax motor controller over CAN bus."""

    _motor: SPARK_TYPE

    def __init__(
        self,
        can_id: int,
        type: CANMotorType,
        brushType: rev.SparkLowLevel.MotorType = rev.SparkLowLevel.MotorType.kBrushless,
    ):
        super().__init__()
        self._motor = type.value(can_id, brushType)
        self._motorConfig = rev.SparkMaxConfig()
        self._stop: bool = False
        self.encoder = self._motor.getEncoder()
        self.pid: Pid | None = None

    def update(self) -> None:
        """
        Updates the motor output if it is not stopped and a pid is set
        """
        if not self._stop and self.pid is not None:
            self.pid.update()
            self._motor.set(self.pid.getOutput())

    def setInverted(self, inv: bool) -> None:
        self._motorConfig.inverted(inv)
        self._configure()

    def setBrakeMode(self, mode: bool) -> None:
        """
        Sets the idle mode
        mode: False = coast, True = Brake
        """
        self._motorConfig.setIdleMode(
            rev.SparkBaseConfig.IdleMode.kBrake
        ) if mode else self._motorConfig.setIdleMode(
            rev.SparkBaseConfig.IdleMode.kCoast
        )

        self._configure()

    def _configure(self) -> None:
        """Updates the motor config"""
        self._motor.configure(
            self._motorConfig,
            rev.ResetMode.kResetSafeParameters,
            rev.PersistMode.kPersistParameters,
        )

    def set_speed(self, speed: float) -> None:
        """Sets the speed of the motor. IF the pid Has been set"""

        if self.pid is not None:
            self._stop = False
            self.pid.setTarget(speed)
            self._motor.set(self.pid.getOutput())
        else:
            print(f"{TAG} Cannot set speed, no pid")

    def set_output(self, output: float) -> None:
        """Set the raw output of the motor."""
        self._motor.set(output)
        if output == 0:
            self._stop = True

    def set_pid(self, pid: Pid) -> None:
        self.pid = pid

    def velocityGetter(self) -> Callable[[], float]:
        """
        returns encoder velocity getter reference
        """
        return self.encoder.getVelocity

    def positionGetter(self) -> Callable[[], float]:
        """
        returns encoder position getter reference
        """
        return self.encoder.getPosition

    def resetEncoder(self) -> None:
        """
        resets the motor's encoder
        """
        self.encoder.setPosition(0.0)

    def stop(self) -> None:
        """Stop motor."""
        self._stop = True
        self._motor.set(0.0)
