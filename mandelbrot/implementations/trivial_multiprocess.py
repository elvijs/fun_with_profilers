"""
The simplest possible implementation of the Mandelbrot set,
but now parallelise to multiple processes.
"""
import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor
from typing import Sequence

import mandelbrot
import mandelbrot.implementations.trivial as trivial_impl


def main(grid_side_size: int, max_iter: int,) -> trivial_impl.TrivialMandelbrotOutput:
    """
    Each row of the mandelbrot pixels is wrapped up in a separate job.
    The jobs are then shoved into the executor.
    """
    executor = ProcessPoolExecutor(max_workers=multiprocessing.cpu_count())

    row_futures = []
    for i in range(grid_side_size):  # fills the i-th row
        row_futures.append(executor.submit(compute_row, i, grid_side_size, max_iter))

    rows = [row_future.result() for row_future in row_futures]
    return rows


def compute_row(i_: int, grid_side_size: int, max_iter: int) -> Sequence[bool]:
    row_ = []
    for j in range(grid_side_size):
        # compute the (i, j)-th grid location in the axis-parallel grid
        # between [-1, -1] and [1, 1]
        c_ij = complex(2 * i_ / grid_side_size - 1, 2 * j / grid_side_size - 1)
        row_.append(trivial_impl.eval_mandelbrot_escape(c_ij, max_iter=max_iter))
    return row_


if __name__ == "__main__":
    args = mandelbrot.parsed_mandelbrot_args()
    result = main(args.grid_side_size, args.max_iter)
    if args.plot:
        trivial_impl.plot(result, save_to="trivial_multiprocess_mandelbrot.png")
