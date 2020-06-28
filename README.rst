========
Overview
========

This package plays around with various profilers through the lens of Mandelbrot set computers.
Heavily inspired by "High Performance Python" by Gorelick & Ozsvald.

* Run the scripts in ``mandelbrot.profilers`` to interact with the (basic) profiler integrations.
* Run the scripts in ``mandelbrot.implementations`` to interact with
  the different Mandelbrot set implementations.

=====
Setup
=====

We use a standard `Poetry <https://python-poetry.org/>`_ setup.

Caveats:

* For me, ``poetry shell`` does not work in PyCharm. Always use a fresh standalone terminal.
  This is relevant for profilers that run outside the Python interpreter.
* Depending on your poetry install, you may have to run ``source $HOME/.poetry/env`` before running any poetry commands.

====
TODO
====

Profilers:

* is there a good profiler for tracking multi-process applications?

Mandelbrot implementations:

* A pure CUDA version, maybe using `PyCUDA <https://documen.tician.de/pycuda/>`_?
  Or maybe `cupy <https://docs-cupy.chainer.org/en/stable/>`_?
* the naive implementation, but threaded
* the naive implementation, but multi-process
* C implementations, see Chapter 7 in "High Performance Python".
* A Rust implementation, see `PyO3 <https://github.com/PyO3/pyo3>`_.
