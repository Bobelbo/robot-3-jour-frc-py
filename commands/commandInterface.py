from subsystems.remote import RemoteControllerSS

class CommandInterface:
    """Default Command Interface and behaviour"""
    def __init__(self, btn_id):
        self._btn_id = btn_id

    def execute(self, input) -> None:
        self._update(input)

        if self._condition(input):
            self._trigger(input)
    
    def bind(self) -> None:
        """Should only be called once, binds itself to remote controller singleton"""
        RemoteControllerSS().bind(self._btn_id, self)

    def _update(self, btn_v) -> None:
        pass

    def _condition(self, btn_v) -> bool:
        return True

    def _trigger(self, btn_v) -> None:
        raise NotImplementedError("Execute method must be implemented by subclasses.")
