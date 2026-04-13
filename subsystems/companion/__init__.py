"""Second example mechanism for superstructure coordination demos."""

from enum import IntEnum, auto

from commands2 import cmd

from subsystems import StateSubsystem


class CompanionSubsystem(StateSubsystem):
    """Placeholder for a second mechanism (feeder, indexer, etc.)."""

    class SubsystemState(IntEnum):
        STOP = auto()
        FORWARD = auto()

    def __init__(self) -> None:
        super().__init__("Companion", self.SubsystemState.STOP)

    def periodic(self) -> None:
        """Students: read ``get_state()`` here and command motors / sim."""
        super().periodic()

    def set_desired_state_command(self, state: SubsystemState):
        """Return a command that sets state (useful for autos)."""
        return cmd.runOnce(lambda: self.set_desired_state(state), self)
