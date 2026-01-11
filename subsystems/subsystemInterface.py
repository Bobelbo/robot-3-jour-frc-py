class SubsystemInterface:
    def update(self) -> None:
        """Method to update the subsystem state."""
        raise NotImplementedError("Update method must be implemented by subclasses.")