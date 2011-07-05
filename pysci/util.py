# util.py

"""Supporting functions for PySci.
"""

def bgr_int_to_rgb(bgr_int):
    """Convert an integer in BGR format to an ``(r, g, b)`` tuple.

    ``bgr_int`` is an integer representation of an RGB color, where the R, G,
    and B values are in the range (0, 255), and the three channels are comined
    into ``bgr_int`` by a bitwise ``red | (green << 8) | (blue << 16)``. This
    leaves the red channel in the least-significant bits, making a direct
    translation to a QColor difficult (the QColor constructor accepts an
    integer form, but it assumes the *blue* channel is in the least-significant
    bits).

    Examples:

        >>> bgr_int_to_rgb(4227327)
        (255, 128, 64)

    """
    red, green, blue = (
        bgr_int         & 0xFF,
        (bgr_int >> 8)  & 0xFF,
        (bgr_int >> 16) & 0xFF,
    )
    return (red, green, blue)


def rgb_to_bgr_int(rgb_tuple):
    """Convert an ``(r, g, b)`` tuple into an integer BGR value.
    Converse of `bgr_int_to_rgb`.
    """
    red, green, blue = rgb_tuple
    return red | (green << 8) | (blue << 16)


