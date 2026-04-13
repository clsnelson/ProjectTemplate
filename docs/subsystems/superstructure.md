# Superstructure

Code: [`subsystems/superstructure.py`](../../subsystems/superstructure.py)

## What it is for

On a real robot, several mechanisms must work together (intake, indexer, shooter, hood, turret). If each button toggles motors independently, mechanisms **fight** each other or leave the robot in an unsafe state.

The **superstructure** is a single `commands2.Subsystem` that owns a small set of **Goals** (high-level intentions). Each goal maps to **subsystem states** in one place. Drivers and autonomous routines request goals; the superstructure applies the right combination of states.

This template uses two placeholder mechanisms:

- **Example** — pretend “intake” (`IDLE` / `ACTIVE`)
- **Companion** — pretend “feeder” (`STOP` / `FORWARD`)

Your competition code can follow the same pattern with real subsystems.

## Goals in this template

| Goal | Example | Companion | Typical teaching point |
|------|---------|-----------|-------------------------|
| `DEFAULT` | `IDLE` | `STOP` | Safe idle home |
| `RUN_EXAMPLE_ONLY` | `ACTIVE` | `STOP` | One mechanism on |
| `RUN_COMPANION_ONLY` | `IDLE` | `FORWARD` | Another on |
| `RUN_BOTH` | `ACTIVE` | `FORWARD` | Coordinated scoring-like mode |

## How goals become motor commands

1. A button or auto schedules `superstructure.set_goal_command(SomeGoal)`.
2. `_set_goal` looks up the row for that goal (`_row_for_goal`).
3. For each subsystem, if the row supplies a state **and** that subsystem exists on this robot, `set_desired_state` is called.
4. Each subsystem’s `periodic()` (override in your code) reads `get_state()` and writes to hardware IO.

Optional logic that depends on **multiple** readings (sensors, “ready to feed”) belongs in `Superstructure.periodic()` on the real robot, similar to how the team codebase gates the feeder until turret, hood, and flywheel are on target.

## Optional mechanisms

`robot_config.has_subsystem("companion")` can be `False` on a practice chassis. The superstructure still runs; states for a missing subsystem are skipped. This template also **gates** `RUN_BOTH` if there is no companion (see `Superstructure.periodic()`).

## Adding a new goal

1. Add a `Goal` enum member in `superstructure.py`.
2. Add a `case` branch in `_row_for_goal` with the desired subsystem states.
3. Bind a button or register a PathPlanner named command with `set_goal_command(...)`.
4. Document the binding in `docs/core/controller-bindings.md`.

## See also

- [implementing-subsystems.md](implementing-subsystems.md)
- [../core/controller-bindings.md](../core/controller-bindings.md)
