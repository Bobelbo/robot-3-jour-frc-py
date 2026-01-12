from typing import List, overload
from subsystems.remote import RemoteControllerSS

class CommandInterface:
    """Default Command Interface and behaviour"""
    @overload
    def __init__(self, btn_id: List[str]):
        ...
    @overload
    def __init__(self, btn_id: str):
        ...
    def __init__(self, btn_id):
        if type(btn_id) is str:
            btn_id = [btn_id]
        self._btn_ids = btn_id            

    def bind(self, controller: 'RemoteControllerSS') -> None:
        """Should only be called once, binds itself to remote controller singleton"""
        for i in range(len(self._btn_ids)):
            controller.bind(self._btn_ids[i], self, i)

    def execute(self, input, index) -> None:
        """Buttons can have indexes for multiple buttons per command"""
        self._update(input, index)

        if self._condition(input, index):
            self._trigger(input, index)

    # ALL THE FUNCTIONS BELLOW SHOULD BE OVERWRITEN (at least trigger)

    def _update(self, btn_v) -> None:
        """Should be used to update command state and pre-calculate for _condition"""
        pass

    def _condition(self, btn_v) -> bool:
        """Should be used as a guard clause not a condition, ie if btn6 is pressed or limit siwitchX is on do not go"""
        return True

    def _trigger(self, btn_v) -> None:
        """Should be used to trigger actuators"""
        raise NotImplementedError("Execute method must be implemented by subclasses.")
