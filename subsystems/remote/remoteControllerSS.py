from ..subsystemInterface import SubsystemInterface
from .remoteInput import RemoteInput


class RemoteControllerSS(SubsystemInterface):
    inputs: dict[str, RemoteInput[bool] | RemoteInput[float]] = {}

    def __init__(self, config):
        """For initialization with config"""
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

    def bind(self, input_id: str, command, index: int) -> None:
        """Method to bind a command to a specific input."""
        self.inputs[input_id].subscribe(command, index)

    def get_input(self, input_id: str) -> RemoteInput[bool] | RemoteInput[float]:
        """Method to get a specific input by its ID."""
        return self.inputs[input_id]
