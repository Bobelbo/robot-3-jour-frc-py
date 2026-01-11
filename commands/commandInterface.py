from subsystems.remote import RemoteControllerSS

class CommandInterface:
    """Default Command Interface and behaviour"""
    def __init__(self, btn_id):
        self._btn_id = btn_id

    def execute(self, input) -> None:
        self._update(input)

        if self._condition(input):
            self._trigger(input)
    
    def bind(self, controller: 'RemoteControllerSS') -> None:
        """Should only be called once, binds itself to remote controller singleton"""
        controller.bind(self._btn_id, self)

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
