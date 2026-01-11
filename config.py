import wpilib
import rev

from commands import tankjoystickCommand

config = {
    'commands': [
        # Initialize your commands here
        tankjoystickCommand(
            wpilib.Joystick(0),
            [
                rev.CANSparkMax(1, rev.CANSparkMax.MotorType.kBrushless),
                rev.CANSparkMax(2, rev.CANSparkMax.MotorType.kBrushless),
            ],
            [
                rev.CANSparkMax(3, rev.CANSparkMax.MotorType.kBrushless),
                rev.CANSparkMax(4, rev.CANSparkMax.MotorType.kBrushless),
            ],
            ),
    ]
}
