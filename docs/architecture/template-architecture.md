# Template Architecture

This project intentionally separates reusable structure from game-specific logic.

```mermaid
flowchart TB
    robotPy[robot.py]
    container[robot_container.py]
    subpackages[subsystems]
    constants[constants.py]
    config[robot_config.py]
    docs[docs]
    tests[tests]

    robotPy --> container
    container --> subpackages
    container --> constants
    container --> config
    subpackages --> tests
    docs --> subpackages
```

## Design rules

1. Keep game-specific constants and behaviors isolated.
2. Keep reusable subsystem patterns generic.
3. Build hardware interaction behind IO abstractions.
4. Require docs updates with behavior changes.