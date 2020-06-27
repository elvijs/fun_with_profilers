"""
Line-by-line profiling of RAM use of Python scripts in :mod:`mandelbrot.implementations` using :mod:`memory_profiler`.
"""
import memory_profiler

import mandelbrot


if __name__ == '__main__':
    args = mandelbrot.parsed_mandelbrot_args()

    for impl in mandelbrot.all_implementations():
        print(f"About to profile {impl.id_}")

        profile = memory_profiler.LineProfiler()
        profile.add_function(impl.callable)
        cmd = f"{impl.fully_qualified_name}(grid_side_size={args.grid_side_size}, max_iter={args.max_iter})"
        global_ns = globals()
        local_ns = locals()
        profile.runctx(cmd, global_ns, local_ns)
        memory_profiler.show_results(profile)
