from pathlib import Path
from random import randrange
from random import choice
import math
from xml.dom import minidom
import svg
from textwrap import dedent

TARGET_FILE = Path("test.svg").resolve()

WIDTH = 1500
HEIGHT = 500
BORDER = 0

CENTERX = round(WIDTH / 2)
CENTERY = round(HEIGHT / 2)


def css_text():
    color = """
        circle {
            fill: light-dark(red, green);
            }
        """

    return dedent(color)


def draw() -> svg.SVG:
    circle = svg.Circle(
        cx=CENTERX,
        r=200,
        # fill="pink",
    )

    return svg.SVG(
        overflow="hidden",
        viewBox=svg.ViewBoxSpec(
            0,
            0,
            WIDTH,
            HEIGHT,
        ),
        elements=[
            circle,
            svg.Style(text=css_text()),
        ],
    )


if __name__ == "__main__":
    result = draw()

    with open(TARGET_FILE, "w", encoding="UTF-8") as f:
        f.write(result.as_str())
