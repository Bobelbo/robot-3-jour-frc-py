# import rev
# import wpilib

# from commands import CommandInterface

# SPARK_TYPE = rev.SparkMax | rev.SparkFlex


# class TurretAngle(CommandInterface):
#     def __init__(
#         self,
#         joystick: wpilib.Joystick,
#         hMotor: SPARK_TYPE,
#         vMotor: SPARK_TYPE,
#     ):
#         self.joystick = joystick
#         self.hMotor = hMotor
#         hMotorConfig = rev.SparkMaxConfig()
#         hMotorConfig.setIdleMode(rev.SparkBaseConfig.IdleMode.kBrake)
#         self.hMotor.configure(
#             hMotorConfig,
#             rev.ResetMode.kResetSafeParameters,
#             rev.PersistMode.kPersistParameters,
#         )
#         self.vMotor = vMotor
#         vMotorConfig = rev.SparkMaxConfig()
#         vMotorConfig.setIdleMode(rev.SparkBaseConfig.IdleMode.kBrake)
#         self.vMotor.configure(
#             vMotorConfig,
#             rev.ResetMode.kResetSafeParameters,
#             rev.PersistMode.kPersistParameters,
#         )

#     def _update(self) -> None:
#         return super()._update()

#     def _condition(self) -> bool:
#         return True

#     def _trigger(self) -> None:
#         hCommand = self.joystick.getRawAxis(0)
#         vCommand = self.joystick.getRawAxis(1)

#         if hCommand >= 0.1:
#             self._hMove(hCommand)

#         if vCommand >= 0.1:
#             self._vMove(vCommand)

#     def _hMove(self, command: float):
#         inputTransform: float = 0.2
#         command = command * inputTransform

#         self.hMotor.set(command)

#     def _vMove(self, command: float):
#         inputTransform: float = 0.1
#         command = command * inputTransform

#         self.vMotor.set(command)
