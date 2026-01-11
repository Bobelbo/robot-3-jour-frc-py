from typing import Generic, List, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from commands.commandInterface import CommandInterface
    
from subsystems.subsystemInterface import SubsystemInterface

# Generic type for RemoteInput
T = TypeVar('T')
class RemoteInput(SubsystemInterface, Generic[T]):
    """Generic class to handle remote inputs and dispatch them"""
    _data_function: lambda: T
    _state: T

    _dirty: bool
    _listeners: List['CommandInterface']

    def __init__(self, data_function: lambda: T):
        """
        :param data_function: Function to gather the button input state
        """
        super().__init__()
        self.data_function = data_function
        self._dirty = False
        self._listeners = []

    def subscribe(self, command: 'CommandInterface') -> None:
        """Method to subscribe a command to this input."""
        self._listeners.append(command)

    def update(self) -> None:
        """Method to update the input state. Also validates the dirtiness to trigger commands correctly."""
        previous_state = self._state
        self._state = self._data_function()
        if self._state != previous_state:
            self._dirty = True
        else:
            self._dirty = False

    def execute(self) -> None:
        if self._dirty:
            for listener in self._listeners:
                listener.execute()

    def consume(self) -> T:
        """
            Method to consume the current button state.
            After calling this method, the state is reset to None, preventing further commands or modules of using the input.
            WIP
        """
        current_state = self._state
        self._state = None
        self._dirty = False
        return current_state
    
    def get(self) -> T:
        """Method to get the current button state. Used by non-subscribers"""
        return self._state
