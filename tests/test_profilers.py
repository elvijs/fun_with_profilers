import os
import pathlib
import subprocess
from typing import Iterator


def test_profilers__do_not_smoke() -> None:
    profilers = _all_python_profilers()

    for profiler_path in profilers:
        cmd = ["python", str(profiler_path), "1", "1"]
        subprocess.check_call(cmd)


def _all_python_profilers() -> Iterator[pathlib.Path]:
    this_file = os.path.realpath(__file__)
    profilers = pathlib.Path(this_file).parent.parent / "mandelbrot" / "profilers"
    return (path for path in profilers.glob("*.py"))
