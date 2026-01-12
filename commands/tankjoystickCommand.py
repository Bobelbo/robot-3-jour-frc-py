from typing import List

from commands import CommandInterface
from subsystems import CANMotorSS, Pid


class TankJoystickCommand(CommandInterface):
    """Tank drive control using a joystick."""
    _axis_deadzone: float = 0.05
    _forward_axis: float
    _rotation_axis: float

    def __init__(self, btn_id: str, leftMotors: List[CANMotorSS], rightMotors: List[CANMotorSS]):
        super().__init__(btn_id)
        self.left_motors = leftMotors
        self.right_motors = rightMotors

        motor: CANMotorSS
        for motor in self.left_motors:
            motor.setBrakeMode(False)
            motor.setInverted(True)
        for motor in self.right_motors:
            motor.setBrakeMode(False)
            motor.setInverted(False)

        self._lpid = Pid(
            dataGetter=self.left_motors[0].getEncoder().getVelocity,
            kp=0.1,
            ki=0.0001,
            tolerance=5,
            noReverse=True 
        )

        self._rpid = Pid(
            dataGetter=self.right_motors[0].getEncoder().getVelocity,
            kp=0.1,
            ki=0.0001,
            tolerance=5,
            noReverse=True 
        )

        self._on = True


    def _update(self, btn_v: int, index: int):
        for motor in self.left_motors + self.right_motors:
            self._updateMotor(motor)

        if index == 2 and btn_v == 1:
            self._on = not self._on
            

    def _condition(self):
        return self._on
    

    def _trigger(self, btn_v: float, index: int) -> None:
        # if value delta is smaller than deadzone threshold, set to 0
        if index == 0 and abs(btn_v) < self._axis_deadzone:
            self._forward_axis = 0
        elif index == 0:
            self._forward_axis = btn_v
        elif index == 1 and abs(btn_v) < self._axis_deadzone:
            self._rotation_axis = 0
        elif index == 1:
            self._rotation_axis = btn_v

        leftspeed = self._forward_axis + self._rotation_axis
        rightspeed = self._forward_axis - self._rotation_axis

        for motor in self.left_motors:
            motor.set_speed(leftspeed)
        for motor in self.right_motors:
            motor.set_speed(rightspeed)


    
    def _updateMotor(self, motor: CANMotorSS):
            if self._on:
                motor.update()
            else:
                motor.stop()