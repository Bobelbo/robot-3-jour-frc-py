import wpilib
import rev

from commands import TankJoystickCommand

config = {
    'commands': [
        # Initialize your commands here
        TankJoystickCommand(
            wpilib.Joystick(0),
            [
                rev.SparkMax(1, rev.SparkLowLevel.MotorType.kBrushless),
                rev.SparkMax(2, rev.SparkLowLevel.MotorType.kBrushless),
            ],            
            [
                rev.SparkMax(3, rev.SparkLowLevel.MotorType.kBrushless),
                rev.SparkMax(4, rev.SparkLowLevel.MotorType.kBrushless),
            ],
            ),
        FeederButtonCommand(
            wpilib.Joystick(3),
            rev.SparkFlex(5, rev.SparkLowLevel.MotorType.kBrushless),
            )
    ]
}
