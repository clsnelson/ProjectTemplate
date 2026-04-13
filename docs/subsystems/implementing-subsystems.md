# Implementing subsystems (and wiring the superstructure)

This template is meant to be copied each season. Follow the same shape for every new mechanism.

## 1. Folder layout

For a mechanism named `intake`:

```text
subsystems/intake/
  __init__.py   # IntakeSubsystem logic + states
  io.py         # IntakeIO, IntakeIOTalonFX, IntakeIOSim
```

Start by **copying** `subsystems/example/` and renaming classes, files, and CAN IDs.

## 2. State pattern

Inherit [`StateSubsystem`](../../subsystems/__init__.py) (or write your own base):

- Define `SubsystemState` as an `IntEnum`.
- Store the current state in the base class.
- Implement `periodic()` to read `get_state()` and call your IO layer (`set_voltage`, `set_position`, etc.).

Keep **state transitions** in `set_desired_state` or small helper methods so commands stay thin.

## 3. IO layer

Put hardware-specific code in `io.py`:

- **`SubsystemIO`** — abstract class: `update_inputs`, `set_*` methods.
- **`SubsystemIOTalonFX`** — real robot.
- **`SubsystemIOSim`** — simulation.

[`subsystems/example/io.py`](../../subsystems/example/io.py) is a minimal stub you can extend.

In [`robot_container.py`](../../robot_container.py), construct the correct IO class based on `Constants.CURRENT_MODE` (real vs sim) the way your team does on the competition robot.

## 4. Register availability

Edit [`robot_config.py`](../../robot_config.py):

- Add the mechanism name to `comp_subsystems` and/or `practice_subsystems`.
- Instantiate the subsystem in `RobotContainer.__init__` only when `has_subsystem("intake")` is true.

That way a practice bot without hardware does not open missing CAN devices.

## 5. Superstructure integration

Open [`subsystems/superstructure.py`](../../subsystems/superstructure.py):

1. Add constructor parameters for new subsystems (`Optional[...] = None`).
2. Store them on `self`.
3. Extend `Goal` and `_row_for_goal` so each goal sets the right combination of states.
4. Add cross-subsystem checks in `periodic()` when needed (locks, sequencing, “ready” logic).

Keep **game-specific constants** (hub pose, PID) in `constants.py`, not inside the superstructure class, unless you have a strong reason.

## 6. Commands and buttons

- Prefer **`superstructure.set_goal_command(Goal.…)`** for coordinated behavior.
- Use **subsystem commands** only for simple overrides, tests, or mechanisms outside the superstructure.

Document every binding in [`docs/core/controller-bindings.md`](../core/controller-bindings.md).

## 7. Autonomous and PathPlanner

Register named commands that call `set_goal_command` with the same goals drivers use. That keeps auto and teleop behavior aligned.

## Checklist before merge

- [ ] Subsystem `periodic()` applies state to IO.
- [ ] `robot_config` updated for which robot has the mechanism.
- [ ] Superstructure goals updated if the mechanism participates in scoring.
- [ ] Docs and controller bindings updated.
