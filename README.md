# Turkuaz ClickFlow

Turkuaz ClickFlow is a desktop automation application for safe, controlled click workflows.

## Sprint-1 Scope

Sprint-1 focuses on the domain foundation for the MVP auto clicker:

- CPS policy: minimum 1, maximum 100, default 10
- Automation state definitions
- Automation settings model
- Click counter reset and increment behavior
- Stop reason definitions

Out of scope for this step:

- PySide6 UI implementation
- Mouse click implementation
- Global hotkey implementation
- Platform adapter implementation

## Technology Decision

- Language: Python
- UI framework: PySide6
- Architecture: platform-independent domain and app logic with Windows/macOS platform adapters

## Project Layout

```text
src/turkuaz_clickflow/
├── app/
├── config/
├── domain/
├── platform/
│   ├── macos/
│   └── windows/
└── ui/
    ├── viewmodels/
    └── views/
```

## Tests

Run unit tests with:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests/unit
```
