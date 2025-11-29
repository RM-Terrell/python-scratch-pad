# Python 3.14 Scratch Pad

A lightweight, isolated development environment designed for writing Python code, solving algorithm challenges, running benchmarks, or any other Python experimentation without polluting or depending on your local machine.

Built on **VS Code Dev Containers**, this project provides a zero-configuration setup for Python code using the latest, fastest tooling available.

## Current Features

* **Python 3.14**: Runs on the bleeding-edge version of Python.
* **uv**: Package manager (replaces pip, poetry, and virtualenv).
* **Ruff**: Linter and formatter (pre-configured to fix on save).
* **Pytest**: Industry-standard unit testing.
* **Pytest-Benchmark**: Benchmarking for Python functions.

## Getting Started

### Prerequisites

1. [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. [VS Code](https://code.visualstudio.com/).
3. [Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for VS Code.

### Installation

1. Clone this repository onto your local machine (host OS shouldn't matter)
2. Open the folder in VS Code (`cd /into/your/dir/path` and `code .`)
3. A popup will appear asking to **"Reopen in Container"**. Click it.
    * *Alternatively: Open Command Palette (`Cmd+Shift+P`) -> "Dev Containers: Reopen in Container".*

The container will build, install Python, and sync dependencies automatically.

## Usage Guide

### Package Management (uv)

This project uses [uv](https://github.com/astral-sh/uv) to manage dependencies and python code execution including the env.

| Goal | Command |
| :--- | :--- |
| **Run a script** | `uv run my_script.py` |
| **Add a library** | `uv add requests` |
| **Add a dev tool** | `uv add --dev numpy` |
| **Sync environment** | `uv sync` |

### Running Tests

Tests are located in the `tests/` directory.

**VS Code:** Go to the "Testing" beaker icon in the sidebar to run/debug tests visually.

**Terminal:**

| Goal | Command |
| :--- | :--- |
| **Run all tests** | `uv run pytest` |
| **To run only benchmarks** | `uv run pytest --benchmark-only` |
| **To run only unit tests** | `uv run pytest --benchmark-skip` |
| **To run tests matching the word "check"** | `uv run pytest -k "check"` |

### Ruff Commands

**Terminal:**

| Goal | Command |
| :--- | :--- |
| **Lint all files** | `uv run ruff check .` |
| **Format all files** | `uv run ruff format .` |
