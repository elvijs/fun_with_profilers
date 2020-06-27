""" Simple timing of Python scripts in :mod:`mandelbrot.implementations` using :mod:`timeit`. """

import statistics
import timeit

import mandelbrot


if __name__ == '__main__':
    args = mandelbrot.parsed_mandelbrot_args()
    num_runs = 10

    for impl in mandelbrot.all_implementations():
        timings = timeit.repeat(
            lambda: impl.callable(grid_side_size=args.grid_side_size, max_iter=args.max_iter),
            number=num_runs,
        )
        mean = statistics.mean(timings)
        stdev = statistics.stdev(timings)
        print(f"{impl.id_} timing: {mean:.2} (stdev: {stdev:.2}) over {num_runs} runs")
