# import rev
# import wpilib

# from commands import CommandInterface


# class FeederAngleCommand(CommandInterface):
#     button: wpilib.Joystick
#     motor: rev.SparkFlex

#     def __init__(self, joystick, motor):
#         self.joystick = joystick
#         self.motor = motor

#     def _update(self) -> None:
#         return super()._update()

#     def _condition(self) -> bool:
#         return True

#     def _trigger(self) -> None:
#         upButton = self.joystick.getRawButton(11)
#         downButton = self.joystick.getRawButton(10)
#         self.motor.set(0.1 * (upButton - downButton))
