"""Main robot entry point for yearly template projects."""

from commands2 import CommandScheduler
from wpilib import TimedRobot

from robot_container import RobotContainer


class Robot(TimedRobot):
    """Season robot class."""

    def robotInit(self) -> None:
        self.container = RobotContainer()

    def robotPeriodic(self) -> None:
        CommandScheduler.getInstance().run()

    def autonomousInit(self) -> None:
        auto = self.container.get_autonomous_command()
        if auto is not None:
            auto.schedule()

    def teleopInit(self) -> None:
        auto = self.container.get_autonomous_command()
        if auto is not None:
            auto.cancel()