"""Shared subsystem helpers."""

from commands2 import Subsystem


class StateSubsystem(Subsystem):
    """Simple stateful subsystem base for template projects."""

    def __init__(self, name: str, initial_state: int) -> None:
        super().__init__()
        self._name = name
        self._state = initial_state

    def periodic(self) -> None:
        """Override in subclasses to apply ``_state`` to hardware or sim."""

    def set_desired_state(self, desired_state: int) -> bool:
        if desired_state == self._state:
            return False
        self._state = desired_state
        return True

    def get_state(self) -> int:
        return self._state