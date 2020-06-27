""" Python memory allocation analysis for scripts in :mod:`mandelbrot.implementations` using :mod:`tracemalloc`. """
import tracemalloc

import mandelbrot

if __name__ == "__main__":
    args = mandelbrot.parsed_mandelbrot_args()

    for impl in mandelbrot.all_implementations():
        tracemalloc.start()
        snapshot_before = tracemalloc.take_snapshot()
        impl.callable(
            grid_side_size=args.grid_side_size, max_iter=args.max_iter
        )
        snapshot_after = tracemalloc.take_snapshot()

        stats = snapshot_after.compare_to(snapshot_before, "lineno")

        print(f"Top 10 memory hogs for {impl.id_}:")
        for stat in stats[:10]:
            print(stat)
