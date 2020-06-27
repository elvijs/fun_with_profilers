import importlib
import os
from dataclasses import dataclass
from pathlib import Path
from typing import List, Sequence

from mandelbrot.api import ImplementationID, MandelbrotImplementation


@dataclass
class Implementation:
    id_: ImplementationID
    callable: MandelbrotImplementation
    fully_qualified_name: str


def all_implementation_paths() -> Sequence[Path]:
    this_file = os.path.realpath(__file__)
    implementations_folder = Path(this_file).parent / "implementations"
    return list(
        path
        for path in implementations_folder.glob("*.py")
        if path.name != "__init__.py"
    )


def all_implementations() -> Sequence[Implementation]:
    ret: List[Implementation] = []

    for script_path in all_implementation_paths():
        module_name = script_path.name.replace(".py", "")
        fully_qualified_module = f"mandelbrot.implementations.{module_name}"
        try:
            module = importlib.import_module(fully_qualified_module)
        except ImportError as err:
            raise Exception(
                f"Could not import an expected Mandelbrot implementation "
                f"in module {fully_qualified_module}"
            ) from err

        try:
            implementation_callable = getattr(module, "main")
        except AttributeError as err:
            raise Exception(
                f"Could not find a Mandelbrot implementation in "
                f"a function called `main` in module {fully_qualified_module}"
            ) from err

        ret.append(
            Implementation(
                id_=ImplementationID(module_name),
                callable=implementation_callable,
                fully_qualified_name=f"{fully_qualified_module}.main",
            )
        )

    return ret


if __name__ == "__main__":
    for script in all_implementation_paths():
        print(script)

    for impl in all_implementations():
        print(impl)
