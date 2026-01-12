from commands import CommandInterface
from subsystems.canMotorSS import CANMotorSS


class FeederAngleCommand(CommandInterface):
    _motor: CANMotorSS = None

    def __init__(self, btns, motor):
        super().__init__(btns)
        self._motor = motor

    def _trigger(self, btn_value, btn_index) -> None:
        # Up = 0 down = 1
        if btn_value == 1 and btn_index == 0:
            self._motor.set(0.1 * 1)
        elif btn_value == 1 and btn_index == 0:
            self._motor.set(0.1 * 1)
        else:
            self._motor.set(0)


# from typing import List
# from commands import CommandInterface
# from subsystems.canMotorSS import CANMotorSS


# class FeederAngleCommand(CommandInterface):
#     _motor: CANMotorSS = None
#     _on: bool = True

#     def __init__(self, btn_id: List[str], motor: CANMotorSS):
#         super().__init__(btn_id)
#         self._motor = motor

#     def _update(self, btn_v, i):
#         if i == 1 and btn_v ==1:
#             self._on = not self._on

#     def _condition(self, btn_v):
#         return self._on

#     def _trigger(self, btn_v: float, index: int) -> None:
#         if index == 0:
#             self._btn0Trigger(btn_v)
    
#     def _btn0Trigger(self, value):
#         self._motor.set(0.1 * value)     
