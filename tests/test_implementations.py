import dataclasses

import mandelbrot


def test_implementations__do_not_smoke() -> None:
    implementations = mandelbrot.all_implementations()
    dummy_args = mandelbrot.ParsedArgs(
        grid_side_size=1,
        max_iter=1,
        plot=False,
    )

    for impl in implementations:
        kwargs = dataclasses.asdict(dummy_args)
        kwargs.pop("plot")
        _ = impl.callable(**kwargs)
