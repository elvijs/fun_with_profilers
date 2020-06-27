"""
Python heap memory allocation analysis for scripts in
:mod:`mandelbrot.implementations` using :mod:`muppy`.
"""
from pympler import muppy, summary

import mandelbrot

if __name__ == "__main__":
    args = mandelbrot.parsed_mandelbrot_args()

    for impl in mandelbrot.all_implementations():
        before = summary.summarize(muppy.get_objects())

        impl.callable(grid_side_size=args.grid_side_size, max_iter=args.max_iter)

        after = summary.summarize(muppy.get_objects())
        differences = summary.get_diff(after, before)

        print(f"Memory use by {impl.id_}:")
        summary.print_(differences)
