from enum import IntEnum
from typing import Any, Iterable, NamedTuple

# Re-exported from pyzbar.locations
class Point(NamedTuple):
    x: int
    y: int

class Rect(NamedTuple):
    left: int
    top: int
    width: int
    height: int

# Re-exported from pyzbar.wrapper
class ZBarSymbol(IntEnum):
    NONE = 0
    PARTIAL = 1
    EAN2 = 2
    EAN5 = 5
    EAN8 = 8
    UPCE = 9
    ISBN10 = 10
    UPCA = 12
    EAN13 = 13
    ISBN13 = 14
    COMPOSITE = 15
    I25 = 25
    DATABAR = 34
    DATABAR_EXP = 35
    CODABAR = 38
    CODE39 = 39
    PDF417 = 57
    QRCODE = 64
    SQCODE = 80
    CODE93 = 93
    CODE128 = 128

class Decoded(NamedTuple):
    data: bytes
    type: str
    rect: Rect
    polygon: list[Point]
    quality: int
    orientation: str | None

ORIENTATION_AVAILABLE: bool
EXTERNAL_DEPENDENCIES: list[Any]

def decode(
    image: Any,
    symbols: Iterable[ZBarSymbol] | None = ...,
) -> list[Decoded]:
    """Decodes barcodes in ``image``.

    Args:
        image: ``numpy.ndarray``, ``PIL.Image`` or tuple (pixels, width, height)
        symbols: iterable of ``ZBarSymbol`` to decode; if ``None``, decodes all
            symbol types.

    Returns:
        list of ``Decoded``: the values decoded from barcodes.
    """
    ...
