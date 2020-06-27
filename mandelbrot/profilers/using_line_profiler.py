"""
Line-by-line profiling of CPU use of Python scripts in :mod:`mandelbrot.implementations` using :mod:`line_profiler`.
"""
from line_profiler import LineProfiler

import mandelbrot


if __name__ == '__main__':
    args = mandelbrot.parsed_mandelbrot_args()

    for impl in mandelbrot.all_implementations():
        print(f"About to profile {impl.id_}")
        profile = LineProfiler()
        profile.add_function(impl.callable)
        cmd = f"{impl.fully_qualified_name}(grid_side_size={args.grid_side_size}, max_iter={args.max_iter})"
        profile.run(cmd)
        profile.print_stats()
