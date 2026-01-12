import wpilib

from commands import FeederAngleCommand, FeederButtonCommand
from commands.turretShooter import TurretShooterCommand
from subsystems.canMotorSS import CANMotorSS, CANMotorType

# We define base wpilib instances so we do not create / destroy in each lambda call
_input_remote = wpilib.Joystick(0)

config = {
    # Will be used and imported directly by subsystems and modules
    "controller": {
        "axies": {
            # ID : Function inside a tuple
            ("baseForwardAxis", lambda: _input_remote.getRawAxis(1)),
            ("baseRotationAxis", lambda: _input_remote.getRawAxis(0)),
            ("baseSmoothingAxis", lambda: _input_remote.getRawAxis(2)),
        },
        "buttons": {
            # ID : Function inside a tuple
            ("btn1", lambda: _input_remote.getRawButton(0)),
            ("btn2", lambda: _input_remote.getRawButton(1)),
            ("btn3", lambda: _input_remote.getRawButton(2)),
            ("btn4", lambda: _input_remote.getRawButton(3)),
            ("btn5", lambda: _input_remote.getRawButton(4)),
            ("btn6", lambda: _input_remote.getRawButton(5)),
            ("btn7", lambda: _input_remote.getRawButton(6)),
            ("btn8", lambda: _input_remote.getRawButton(7)),
            ("btn9", lambda: _input_remote.getRawButton(8)),
            ("btn10", lambda: _input_remote.getRawButton(9)),
            ("btn11", lambda: _input_remote.getRawButton(10)),
        },
    },
    # Config for actuators and sensors
    "subsystems": {},
    # List of commands to bind to the robot
    # A command only has one input trigger
    "commands": [
        # Initialize your commands here\
        FeederButtonCommand("btn2", CANMotorSS(5, CANMotorType.SPARKFLEX)),
        FeederAngleCommand(["btn11", "btn10"], CANMotorSS(6, CANMotorType.SPARKMAX)),
        TurretShooterCommand(
            button="btn0",
            shootMotor=CANMotorSS(10, CANMotorType.SPARKFLEX),
            feedMotor=CANMotorSS(11, CANMotorType.SPARKMAX),
        ),
        # TankJoystickCommand(
        #     wpilib.Joystick(0),
        #     [
        #         rev.SparkMax(1, rev.SparkLowLevel.MotorType.kBrushless),
        #         rev.SparkMax(2, rev.SparkLowLevel.MotorType.kBrushless),
        #     ],
        #     [
        #         rev.SparkMax(3, rev.SparkLowLevel.MotorType.kBrushless),
        #         rev.SparkMax(4, rev.SparkLowLevel.MotorType.kBrushless),
        #     ],
        #     ),
    ],
}
