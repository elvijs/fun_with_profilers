import argparse
from dataclasses import dataclass
from typing import Any, NewType, Protocol, Sequence

ImplementationID = NewType("ImplementationID", str)

ESCAPE_THRESHOLD = 2.0


class MandelbrotImplementation(Protocol):
    def __call__(self, grid_side_size: int, max_iter: int) -> Any:
        pass


@dataclass
class ParsedArgs:
    grid_side_size: int
    max_iter: int
    plot: bool


def parsed_mandelbrot_args() -> ParsedArgs:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "grid_side_size",
        help="The number of points along each of the axis of the grid. "
        "We will always only consider points in "
        "the axis-parallel square with two corners in [-1, -1] and [1, 1]. "
        "We will thus consider a total of grid_side_size*grid_side_size points.",
        type=int,
    )
    parser.add_argument(
        "max_iter",
        help="The maximum number of iterations per point. "
        "If the recursion hasn't achieved the escape condition by this point, "
        "then the point is declared to be in the Mandelbrot set.",
        type=int,
    )
    parser.add_argument(
        "-plot", help="Store a plot?", action="store_true",
    )
    args = parser.parse_args()

    return ParsedArgs(
        grid_side_size=args.grid_side_size,
        max_iter=args.max_iter,
        plot=args.plot,
    )
