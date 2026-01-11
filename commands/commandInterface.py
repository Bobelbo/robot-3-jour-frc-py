class CommandInterface:
    def execute(self) -> None:
        raise NotImplementedError("Execute method must be implemented by subclasses.")