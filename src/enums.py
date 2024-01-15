""" Enumeraciones utilizadas en el proyecto. """

import enum


class TextPosition(enum.Enum):
    """Enumeración para las posiciones de los textos."""

    TOP_LEFT = 1
    TOP_CENTER = 2
    TOP_RIGHT = 3

    MIDDLETOP_LEFT = 4
    MIDDLETOP_CENTER = 5
    MIDDLETOP_RIGHT = 6

    MIDDLE_LEFT = 7
    MIDDLE_CENTER = 8
    MIDDLE_RIGHT = 9

    MIDDLEBOTTOM_LEFT = 10
    MIDDLEBOTTOM_CENTER = 11
    MIDDLEBOTTOM_RIGHT = 12

    BOTTOM_LEFT = 13
    BOTTOM_CENTER = 14
    BOTTOM_RIGHT = 15
