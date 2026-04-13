"""Shared constants for the robot template."""

from enum import Enum, auto

from wpilib import RobotBase


class Constants:
    """Container for all robot constants."""

    class Mode(Enum):
        REAL = auto()
        SIM = auto()
        REPLAY = auto()

    SIM_MODE = Mode.SIM
    CURRENT_MODE = Mode.REAL if RobotBase.isReal() else SIM_MODE