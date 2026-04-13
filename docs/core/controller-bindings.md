# Controller bindings (template)

Source: [`robot_container.py`](../../robot_container.py)

## Controllers

| Controller | Port | Role |
|------------|------|------|
| Driver | 0 | Direct subsystem demo (hold **A** on example subsystem) |
| Function | 1 | **Superstructure** goals |

## Driver (0)

| Control | Type | Action |
|---------|------|--------|
| **A** | `whileTrue` | Run `ExampleSubsystem` demo command (bypasses superstructure for teaching) |

## Function (1)

| Button | Type | Superstructure goal |
|--------|------|---------------------|
| **A** | `onTrue` | `DEFAULT` |
| **X** | `onTrue` | `RUN_COMPANION_ONLY` |
| **B** | `onTrue` | `RUN_EXAMPLE_ONLY` |
| **Y** | `onTrue` | `RUN_BOTH` |

On a **practice** configuration without `companion`, `RUN_BOTH` is gated in `Superstructure.periodic()` so the example mechanism does not stay active without the second mechanism.
