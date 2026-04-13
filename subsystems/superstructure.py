"""Superstructure: coordinates multiple mechanisms from high-level goals.

Buttons and autos set a single :class:`Goal` instead of toggling several
subsystems independently. See ``docs/subsystems/superstructure.md``.
"""
from __future__ import annotations

from enum import IntEnum, auto
from typing import Optional

from commands2 import Command, Subsystem, cmd
from wpilib import SmartDashboard

from subsystems.companion import CompanionSubsystem
from subsystems.example import ExampleSubsystem


class Superstructure(Subsystem):
    """Maps :class:`Goal` values to subsystem states."""

    class Goal(IntEnum):
        """High-level robot intentions. Add entries as you add mechanisms."""
        DEFAULT = auto()
        RUN_EXAMPLE_ONLY = auto()
        RUN_COMPANION_ONLY = auto()
        RUN_BOTH = auto()

    def __init__(
        self,
        example: Optional[ExampleSubsystem] = None,
        companion: Optional[CompanionSubsystem] = None,
    ) -> None:
        super().__init__()
        self.example = example
        self.companion = companion
        self._goal_state = self.Goal.DEFAULT
        self._set_goal(self.Goal.DEFAULT)

    def periodic(self) -> None:
        """Telemetry and optional gating between subsystems."""
        SmartDashboard.putString(
            "Superstructure/Goal", self._goal_state.name
        )
        # Example gate: cannot run "both" without a companion mechanism.
        if self._goal_state == self.Goal.RUN_BOTH and self.companion is None:
            if self.example is not None:
                self.example.set_desired_state(
                    ExampleSubsystem.SubsystemState.IDLE
                )

    def _row_for_goal(
        self, goal: Goal
    ) -> tuple[
        Optional[ExampleSubsystem.SubsystemState],
        Optional[CompanionSubsystem.SubsystemState],
        bool,
    ]:
        """Return (example_state, companion_state, update_tracked_goal)."""
        match goal:
            case self.Goal.DEFAULT:
                return (
                    ExampleSubsystem.SubsystemState.IDLE,
                    CompanionSubsystem.SubsystemState.STOP,
                    True,
                )
            case self.Goal.RUN_EXAMPLE_ONLY:
                return (
                    ExampleSubsystem.SubsystemState.ACTIVE,
                    CompanionSubsystem.SubsystemState.STOP,
                    True,
                )
            case self.Goal.RUN_COMPANION_ONLY:
                return (
                    ExampleSubsystem.SubsystemState.IDLE,
                    CompanionSubsystem.SubsystemState.FORWARD,
                    True,
                )
            case self.Goal.RUN_BOTH:
                return (
                    ExampleSubsystem.SubsystemState.ACTIVE,
                    CompanionSubsystem.SubsystemState.FORWARD,
                    True,
                )
            case _:
                return (None, None, False)

    def _set_goal(self, goal: Goal) -> None:
        example_state, companion_state, track = self._row_for_goal(goal)
        if example_state is not None and self.example is not None:
            self.example.set_desired_state(example_state)
        if companion_state is not None and self.companion is not None:
            self.companion.set_desired_state(companion_state)
        if track:
            self._goal_state = goal

    def set_goal_command(self, goal: Goal) -> Command:
        """Apply a goal when the command runs (bind to buttons or PathPlanner)."""
        return cmd.runOnce(lambda g=goal: self._set_goal(g), self)
