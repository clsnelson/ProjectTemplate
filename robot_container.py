"""Template robot container: subsystems, superstructure, and bindings."""

import commands2
from commands2 import cmd

from robot_config import has_subsystem
from subsystems.companion import CompanionSubsystem
from subsystems.example import ExampleSubsystem
from subsystems.superstructure import Superstructure


class RobotContainer:
    """Wires up robot subsystems, superstructure, and operator controls."""

    def __init__(self) -> None:
        self._driver_controller = commands2.button.CommandXboxController(0)
        self._function_controller = commands2.button.CommandXboxController(1)

        self.example: ExampleSubsystem | None = None
        self.companion: CompanionSubsystem | None = None

        if has_subsystem("example"):
            self.example = ExampleSubsystem()
        if has_subsystem("companion"):
            self.companion = CompanionSubsystem()

        self.superstructure = Superstructure(self.example, self.companion)
        # Keep superstructure in the scheduler so :meth:`Superstructure.periodic`
        # runs (telemetry / gating) even before any goal button is pressed.
        self.superstructure.setDefaultCommand(
            cmd.run(lambda: None, self.superstructure)
        )

        self._setup_controller_bindings()

    def _setup_controller_bindings(self) -> None:
        # Driver: quick direct example toggle (teaches subsystem commands).
        if self.example is not None:
            self._driver_controller.a().whileTrue(
                self.example.run_example_command()
            )

        # Function: superstructure goals (teaches coordinated control).
        self._function_controller.y().onTrue(
            self.superstructure.set_goal_command(Superstructure.Goal.RUN_BOTH)
        )
        self._function_controller.b().onTrue(
            self.superstructure.set_goal_command(
                Superstructure.Goal.RUN_EXAMPLE_ONLY
            )
        )
        self._function_controller.x().onTrue(
            self.superstructure.set_goal_command(
                Superstructure.Goal.RUN_COMPANION_ONLY
            )
        )
        self._function_controller.a().onTrue(
            self.superstructure.set_goal_command(Superstructure.Goal.DEFAULT)
        )

    def get_autonomous_command(self) -> commands2.Command:
        """Return autonomous command selection."""
        return cmd.none()
