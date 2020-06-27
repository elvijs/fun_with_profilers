import mandelbrot
import mandelbrot.implementations.trivial


def test_implementation_paths__is_not_smoking() -> None:
    assert len(mandelbrot.all_implementation_paths())


def test_implementation_paths__contains_some_expected_modules() -> None:
    all_paths = mandelbrot.all_implementation_paths()
    minimum_expected_scripts = {"trivial.py", "numexpr_based.py", "numpy_based.py"}
    assert minimum_expected_scripts <= {path.name for path in all_paths}


def test_all_implementations__is_not_smoking() -> None:
    assert len(mandelbrot.all_implementations())


def test_all_implementations__contains_expected_implementations() -> None:
    expected_implementations = {"trivial", "numexpr_based", "numpy_based"}
    assert expected_implementations <= {impl.id_ for impl in mandelbrot.all_implementations()}


def test_all_implementations__correctly_wraps_the_trivial_implementation() -> None:
    ids_to_impls = {impl.id_: impl for impl in mandelbrot.all_implementations()}
    trivial_impl = ids_to_impls["trivial"]

    assert mandelbrot.Implementation(
        id_=mandelbrot.ImplementationID("trivial"),
        callable=mandelbrot.implementations.trivial.main,
        fully_qualified_name="mandelbrot.implementations.trivial.main",
    ) == trivial_impl
