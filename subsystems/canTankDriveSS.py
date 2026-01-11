import rev

from typing import List

class CanTankDriveSS():
    """Subsystem for controlling a tank drive using CAN SparkMax motor controllers."""
    
    def __init__(self, left_motors: List[rev.SparkMax], right_motors: List[rev.SparkMax]):
        super().__init__()
        self.left_motors = left_motors
        self.right_motors = right_motors

    def set_left_speed(self, speed: float) -> None:
        """Set the speed of the left motors."""
        for motor in self.left_motors:
            motor.set(speed)

    def set_right_speed(self, speed: float) -> None:
        """Set the speed of the right motors."""
        for motor in self.right_motors:
            motor.set(speed)

    def stop(self) -> None:
        """Stop all motors."""
        self.set_left_speed(0.0)
        self.set_right_speed(0.0)