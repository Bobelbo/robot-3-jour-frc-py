from typing import List
import math
from commands import CommandInterface
from subsystems import CANMotorSS, CanTankDriveSSAnalog

TAG = "TankJoystickCommand:"
SMOOTHING = 3


class TankJoystickCommand(CommandInterface):
    """Tank drive control using a joystick."""

    _axis_deadzone: float = 0.05

    def __init__(
        self,
        btn_id: List[str],
        left_motors: List[CANMotorSS],
        right_motors: List[CANMotorSS],
    ):
        """Needs two axies, forward and rotation, 3rd button is optional, will be for toggling the base"""
        super().__init__(btn_id)
        self._drive = CanTankDriveSSAnalog(left_motors, right_motors)
        self._drive.stop()

        self._rotation_axis = 0.0  # We put 0.0 to specify it is a float, this allows intellisense to kick in
        self._forward_axis = 0.0
        self._on = True

    def update(self):
        if self._on:
            self._drive.update()
        else:
            self._drive.stop()

    def _update(self, btn_v: int, index: int):
        if index == 2 and btn_v == 1:
            self._on = not self._on

    def _condition(self, btn_v, index: int):
        return self._on

    def _trigger(self, btn_v: float, index: int) -> None:
        # if value delta is smaller than deadzone threshold, set to 0

        if index == 0 and abs(btn_v) < self._axis_deadzone:
            self._forward_axis = 0
        elif index == 0:
            self._forward_axis = math.pow(btn_v, SMOOTHING)
        elif index == 1 and abs(btn_v) < self._axis_deadzone:
            self._rotation_axis = 0
        elif index == 1:
            self._rotation_axis = math.pow(btn_v, SMOOTHING)

        leftspeed = self._forward_axis + self._rotation_axis
        rightspeed = self._forward_axis - self._rotation_axis

        print(f"{TAG} Base right speed: {rightspeed}")
        print(f"{TAG} Base left speed: {btn_v}")

        self._drive.set_left_speed(leftspeed)
        self._drive.set_right_speed(rightspeed)

    def _updateMotor(self, motor: CANMotorSS):
        if self._on:
            motor.update()
        else:
            motor.stop()
