# Template Architecture

This project intentionally separates reusable structure from game-specific logic.

```mermaid
flowchart TB
    robotPy[robot.py]
    container[robot_container.py]
    superstructure[Superstructure]
    subpackages[subsystems]
    constants[constants.py]
    config[robot_config.py]
    docs[docs]
    tests[tests]

    robotPy --> container
    container --> superstructure
    container --> subpackages
    container --> constants
    container --> config
    superstructure --> subpackages
    subpackages --> tests
    docs --> subpackages
```

## Design rules

1. Keep game-specific constants and behaviors isolated.
2. Keep reusable subsystem patterns generic.
3. Coordinate mechanisms through **superstructure goals** when more than one subsystem must stay in sync.
4. Build hardware interaction behind IO abstractions.
5. Require docs updates with behavior changes.