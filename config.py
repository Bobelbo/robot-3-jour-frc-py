import wpilib

from commands import (
    ClimberCommand,
    FeederAngleCommand,
    FeederButtonCommand,
    # TankJoystickCommand,
    TurretAngleCommand,
    TurretShooterCommand,
)
from subsystems import CANMotorSS, CANMotorType, DigitalIO

"""
Here is the approach we used to program the robot:

The config file is used to specify Controller Inputs, Commands and Actuators,

The Controller input should have function that returns updated data for the given input label
The Inputs are either classified as axies (float) or buttons (int)
The Input functions key are used as labels to link input events

The Commands should be instanciated in the config variable.
Each command should be created using the constructor defined in the class.
A command can take either a single input label or an array of input labels.
A command can necessitate motors or digital inputs, in either cases they should be
instanciated and populated with the correct CAN id and minimal configuration.

We want the config to remain as simple and efficient as possible so we can create and edit I/Os on the fly
"""

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
    # List of commands to bind to the robot
    # A command only has one input trigger
    "commands": [
        # Initialize your commands here\
        FeederButtonCommand(
            "btn3",
            motor=CANMotorSS(5, CANMotorType.SPARKFLEX),
        ),
        FeederAngleCommand(
            ["btn11", "btn10"],
            motor=CANMotorSS(6, CANMotorType.SPARKMAX),
            deployed_limit_switch=DigitalIO(0),
        ),
        ClimberCommand(
            ["btn6", "btn7"],
            motor=CANMotorSS(7, CANMotorType.SPARKMAX),
        ),
        TurretShooterCommand(
            "btn1",
            shootMotor=CANMotorSS(10, CANMotorType.SPARKFLEX),
            feedMotors=[
                CANMotorSS(11, CANMotorType.SPARKMAX),
                CANMotorSS(12, CANMotorType.SPARKMAX),
            ],
        ),
        TurretAngleCommand(
            ["baseRotationAxis", "baseForwardAxis", "btn9"],
            horizontal_motor=CANMotorSS(8, CANMotorType.SPARKMAX),
            vertical_motor=CANMotorSS(9, CANMotorType.SPARKMAX),
            vertical_switch=DigitalIO(1),
        ),
    ],
}
