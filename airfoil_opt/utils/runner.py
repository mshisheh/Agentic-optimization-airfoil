"""Generic command runner helpers."""

from __future__ import annotations

import subprocess
from typing import Sequence


def run_command(command: Sequence[str], cwd: str | None = None) -> subprocess.CompletedProcess[str]:
    """Run a command and capture output."""
    return subprocess.run(command, cwd=cwd, check=False, text=True, capture_output=True)
