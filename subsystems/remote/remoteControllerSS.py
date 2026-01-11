from config import config
from .remoteInput import RemoteInput
from ..subsystemInterface import SubsystemInterface

class RemoteControllerSS(SubsystemInterface):
    inputs: dict[str, RemoteInput[bool]|RemoteInput[float]] = {}

    _instance = None

    # @staticmethod
    # def get_instance():
    #     """Static access method."""
    #     if RemoteControllerSS._instance is None:
    #         RemoteControllerSS._instance = RemoteControllerSS()
    #     return RemoteControllerSS._instance

    def __new__(cls):
        """Static access method."""
        if RemoteControllerSS._instance is None:
            RemoteControllerSS._instance = super(RemoteControllerSS, cls).__new__(cls)  
        return RemoteControllerSS._instance

    def __init__(self):
        """SHOULD NOT BE CALLED DIRECTLY. USE get_instance() INSTEAD."""
        for axis_id, axis_func in config.get("axies"):
            self.inputs[axis_id] = RemoteInput(axis_func)

        for btn_id, btn_func in config.get("buttons"):
            self.inputs[btn_id] = RemoteInput(btn_func)

    def update(self) -> None:
        """Method to update the subsystem state."""
        for input in self.inputs.values():
            input.update()

    def execute(self) -> None:
        """Method to execute the subsystem behaviour."""
        for input in self.inputs.values():
            input.execute()

    def bind(self, input_id: str, command) -> None:
        """Method to bind a command to a specific input."""
        self.inputs[input_id].sub.append(command)

    def get_input(self, input_id: str) -> RemoteInput[bool]|RemoteInput[float]:
        """Method to get a specific input by its ID."""
        return self.inputs[input_id]
        
    def __call__(self):
        raise TypeError('Class must be accessed through `get_instance()`.')