"""Example subsystem package for students to copy from."""

from enum import IntEnum, auto

from commands2 import cmd

from subsystems import StateSubsystem


class ExampleSubsystem(StateSubsystem):
    """Minimal subsystem showing the state pattern."""

    class SubsystemState(IntEnum):
        IDLE = auto()
        ACTIVE = auto()

    def __init__(self) -> None:
        super().__init__("Example", self.SubsystemState.IDLE)

    def run_example_command(self):
        return cmd.runEnd(
            lambda: self.set_desired_state(self.SubsystemState.ACTIVE),
            lambda interrupted: self.set_desired_state(self.SubsystemState.IDLE),
            self,
        )