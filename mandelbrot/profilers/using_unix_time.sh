#!/usr/bin/env bash

# TODO: more bash-fu would be useful, for example, we should assert the following files exist and
#  enable the paarames to be passed to the script.
#  Unfortunately that is sufficiently yucky for me to not want to spend time on it right now.

echo "Please ensure you've activated the target venv before running this script (`poetry shell` is the recommended approach, read more about this in the README)"
echo "See https://man7.org/linux/man-pages/man1/time.1.html for the description of the various metrics"

/usr/bin/time --verbose python3.8 ../implementations/numpy_based.py 100 1000
echo ""
/usr/bin/time --verbose python3.8 ../implementations/trivial.py 100 1000
echo ""
/usr/bin/time --verbose python3.8 ../implementations/numexpr_based.py 100 1000
