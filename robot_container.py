"""Template robot container: subsystems, commands, and controller bindings."""

import commands2
from commands2 import cmd

from constants import Constants
from robot_config import has_subsystem
from subsystems.example import ExampleSubsystem


class RobotContainer:
    """Wires up robot subsystems and operator controls."""

    def __init__(self) -> None:
        self._driver_controller = commands2.button.CommandXboxController(0)

        self.example: ExampleSubsystem | None = None

        if has_subsystem("example"):
            self.example = ExampleSubsystem()

        self._setup_controller_bindings()

    def _setup_controller_bindings(self) -> None:
        if self.example is None:
            return

        # Hold A to run the example subsystem action.
        self._driver_controller.a().whileTrue(self.example.run_example_command())

    def get_autonomous_command(self) -> commands2.Command:
        """Return autonomous command selection."""
        # Replace with chooser logic in-season.
        return cmd.none()