import numexpr as ne
import numpy as np

import mandelbrot


def main(grid_side_size: int, max_iter: int) -> np.ndarray:
    X = np.linspace(-1, 1, grid_side_size, dtype=np.float32)
    Y = np.linspace(-1, 1, grid_side_size, dtype=np.float32)
    C = X + Y[:, None] * (-1j)
    Z = np.zeros(C.shape, np.complex64)
    for n in range(max_iter):
        Z = ne.evaluate("Z ** 2 + C")

    TRAPPED = abs(Z) < mandelbrot.ESCAPE_THRESHOLD
    return ~TRAPPED


def plot(data: np.ndarray) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    plt.imshow(data, extent=[-1, 1, -1, 1], interpolation="bicubic")
    plt.savefig("numexpr_mandelbrot.png")


if __name__ == "__main__":
    args = mandelbrot.parsed_mandelbrot_args()
    result = main(args.grid_side_size, args.max_iter)
    if args.plot:
        plot(result)
