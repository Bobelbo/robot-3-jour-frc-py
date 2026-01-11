class CommandInterface:
    """Default Command Interface and behaviour"""
    def execute(self) -> None:
        self._update()

        if self._condition():
            self._trigger()

    def _update(self) -> None:
        pass

    def _condition(self) -> bool:
        return True

    def _trigger(self) -> None:
        raise NotImplementedError("Execute method must be implemented by subclasses.")
