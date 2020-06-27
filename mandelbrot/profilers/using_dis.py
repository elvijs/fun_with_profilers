"""
CPython Bytecode display for Python scripts in :mod:`mandelbrot.implementations`
using :mod:`dis`.
"""
import dis

import mandelbrot

if __name__ == "__main__":
    for impl in mandelbrot.all_implementations():
        print(f"Bytecode for {impl.id_}:")
        dis.dis(impl.callable)
