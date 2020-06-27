""" The simplest possible implementation of the Mandelbrot set. """
from typing import Sequence

import numpy as np

import mandelbrot

TrivialMandelbrotOutput = Sequence[Sequence[bool]]


def eval_mandelbrot_escape(c: complex, max_iter: int) -> bool:
    num_attempts = 0
    z = complex(0, 0)
    while num_attempts < max_iter:
        z = z * z + c
        if abs(z) > mandelbrot.ESCAPE_THRESHOLD:
            return True
        num_attempts += 1
    return False


def main(grid_side_size: int, max_iter: int) -> TrivialMandelbrotOutput:
    rows = []
    for i in range(grid_side_size):  # fills the i-th row
        row_i = []
        for j in range(grid_side_size):
            # compute the (i, j)-th grid location in the axis-parallel grid
            # between [-1, -1] and [1, 1]
            c_ij = complex(2 * i / grid_side_size - 1, 2 * j / grid_side_size - 1)
            row_i.append(eval_mandelbrot_escape(c_ij, max_iter=max_iter))
        rows.append(row_i)

    return rows


def plot(data: TrivialMandelbrotOutput) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    as_nparray = np.array(data)
    plt.imshow(as_nparray, extent=[-1, 1, -1, 1], interpolation="bicubic")
    plt.savefig("trivial_mandelbrot.png")


if __name__ == "__main__":
    args = mandelbrot.parsed_mandelbrot_args()
    result = main(args.grid_side_size, args.max_iter)
    if args.plot:
        plot(result)
