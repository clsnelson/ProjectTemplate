# FRC Python Project Template

This repository is a season-start foundation for FRC teams using RobotPy and command-based architecture.

## What this template provides

- A clean `robot.py` + `robot_container.py` structure.
- A reusable subsystem + IO abstraction pattern.
- Starter `constants.py`, `robot_config.py`, and `util.py`.
- Basic testing entry point in `tests/`.
- Student-friendly docs with onboarding and yearly kickoff checklists.
- Rule-compliance checklist for reusable pre-Kickoff software workflow.

## Intended yearly workflow

1. Keep this template public and version-tagged before Kickoff.
2. Create a new season repo from this template after Kickoff.
3. Add game-specific mechanisms and strategy in the season repo.
4. Keep reusable, game-agnostic improvements here and in shared libraries.

## Quick start

1. Create your new season repo from this template.
2. Update `robot_config.py` with your robot MAC addresses and subsystem map.
3. Update constants in `constants.py` for current hardware and field data.
4. Implement real subsystems under `subsystems/`.
5. Update controller bindings in `robot_container.py`.

## Documentation map

- `docs/README.md` - doc index
- `docs/getting-started/new-season-checklist.md` - kickoff workflow
- `docs/guides/student-onboarding.md` - 4-week student onboarding model
- `docs/guides/r303-compliance-checklist.md` - software reuse compliance process