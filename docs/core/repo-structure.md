# Repository Structure

## Root files

- `robot.py` - robot lifecycle entrypoint
- `robot_container.py` - subsystem construction and bindings
- `constants.py` - centralized constants and run mode selection
- `robot_config.py` - robot identity and subsystem availability map
- `util.py` - shared helper functions

## Key folders

- `subsystems/` - subsystem logic, IO abstraction packages, and `superstructure.py`
- `tests/` - pyfrc/pytest tests
- `docs/` - onboarding, architecture, and process docs

## Copying into a season repo

1. Clone this template into a new season project.
2. Rename/add subsystem packages for this game.
3. Replace example subsystem and bindings with season requirements.
4. Keep docs in sync with every significant code change.