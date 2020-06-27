"""
Simple CPU profiling of Python scripts in :mod:`mandelbrot.implementations`
using :mod:`cProfile`.
"""

import cProfile
import pstats
import tempfile

import mandelbrot

if __name__ == "__main__":
    args = mandelbrot.parsed_mandelbrot_args()

    for impl in mandelbrot.all_implementations():
        cmd = (
            f"{impl.fully_qualified_name}(grid_side_size={args.grid_side_size}, "
            f"max_iter={args.max_iter})"
        )
        print(f"About to profile {cmd}")
        with tempfile.NamedTemporaryFile() as tmp_stats_file:
            cProfile.run(cmd, filename=tmp_stats_file.name)
            stats = pstats.Stats(tmp_stats_file.name)

            stats.sort_stats(pstats.SortKey.CUMULATIVE)  # type: ignore  # MyPy's wrong
            stats.print_title()
            stats.print_stats()
            print("Callers:")
            stats.print_callers()
