"""Example IO abstraction pattern for subsystems."""

from dataclasses import dataclass


class ExampleIO:
    """Abstract IO contract used by subsystem logic."""

    @dataclass(slots=True)
    class Inputs:
        connected: bool = False
        value: float = 0.0

    def update_inputs(self, inputs: Inputs) -> None:
        """Update input values from hardware/sim layer."""

    def set_output(self, output: float) -> None:
        """Set output to hardware/sim layer."""