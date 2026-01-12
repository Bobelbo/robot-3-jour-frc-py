import wpilib

from commands import (
    ClimberCommand,
    FeederAngleCommand,
    FeederButtonCommand,
    TankJoystickCommand,
    TurretAngleCommand,
    TurretShooterCommand,
)
from subsystems import CANMotorSS, CANMotorType, Dio

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
            ("btn1", lambda: _input_remote.getRawButton(1)),
            ("btn2", lambda: _input_remote.getRawButton(2)),
            ("btn3", lambda: _input_remote.getRawButton(3)),
            ("btn4", lambda: _input_remote.getRawButton(4)),
            ("btn5", lambda: _input_remote.getRawButton(5)),
            ("btn6", lambda: _input_remote.getRawButton(6)),
            ("btn7", lambda: _input_remote.getRawButton(7)),
            ("btn8", lambda: _input_remote.getRawButton(8)),
            ("btn9", lambda: _input_remote.getRawButton(9)),
            ("btn10", lambda: _input_remote.getRawButton(10)),
            ("btn11", lambda: _input_remote.getRawButton(11)),
        },
    },
    # Config for actuators and sensors
    "subsystems": {},
    # List of commands to bind to the robot
    # A command only has one input trigger
    "commands": [
        # Initialize your commands here\
        FeederButtonCommand(
            "btn3",
            CANMotorSS(5, CANMotorType.SPARKFLEX),
        ),
        FeederAngleCommand(
            ["btn11", "btn10"],
            CANMotorSS(6, CANMotorType.SPARKMAX),
            Dio(0),
        ),
        ClimberCommand(
            ["btn6", "btn7"],
            CANMotorSS(7, CANMotorType.SPARKMAX),
        ),
        TurretShooterCommand(
            button="btn1",
            shootMotor=CANMotorSS(10, CANMotorType.SPARKFLEX),
            feedMotor=CANMotorSS(11, CANMotorType.SPARKMAX),
        ),
        TurretAngleCommand(
            ["baseRotationAxis", "baseForwardAxis", "btn9"],
            horizontal_motor=CANMotorSS(8, CANMotorType.SPARKMAX),
            vertical_motor=CANMotorSS(9, CANMotorType.SPARKMAX),
        ),
    ],
}
