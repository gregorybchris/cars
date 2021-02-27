"""Utilities for color printing."""

from sty import fg
from typing import Tuple


class Color:
    """Colors for color printing."""

    BLUE = (90, 100, 255)
    GRAY = (130, 130, 130)
    GREEN = (60, 180, 70)
    RED = (200, 80, 90)
    PURPLE = (150, 90, 250)
    WHITE = (190, 190, 190)
    YELLOW = (180, 180, 80)


def print_rgb(s: str,
              rgb: Tuple[int, int, int],
              *args,
              **kwargs):
    """
    Print to stdout with color.
    :param s: String to print to stdout.
    :param rgb: Tuple with rgb values in the range [0, 255].
    """
    print(f"{fg(*rgb)}{s}{fg.rs}", *args, **kwargs)