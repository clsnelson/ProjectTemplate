"""Robot identity and subsystem availability configuration."""

from enum import Enum, auto
from typing import Final


class Robot(Enum):
    COMP = auto()
    PRACTICE = auto()


# Start new seasons on COMP by default; customize for your team.
currentRobot: Final[Robot] = Robot.COMP


def has_subsystem(subsystem_name: str) -> bool:
    """Return whether this robot configuration includes a subsystem."""
    comp_subsystems = {
        "drivetrain",
        "vision",
        "example",
    }

    practice_subsystems = {
        "drivetrain",
        "example",
    }

    if currentRobot == Robot.COMP:
        return subsystem_name.lower() in comp_subsystems
    return subsystem_name.lower() in practice_subsystems