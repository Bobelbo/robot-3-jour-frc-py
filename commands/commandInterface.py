class CommandInterface:
    """Default Command Interface and behaviour"""
    def trigger(self) -> None:
        self._update()

        if self._condition():
            self._execute()

    def _update(self) -> None:
        pass

    def _condition(self) -> bool:
        return True

    def _execute(self) -> None:
        raise NotImplementedError("Execute method must be implemented by subclasses.")
