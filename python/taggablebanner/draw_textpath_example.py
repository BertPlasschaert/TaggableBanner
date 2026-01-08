from pathlib import Path
from random import randrange
from random import choice
import math
from xml.dom import minidom
import svg

TARGET_FILE = Path("tmp.svg").resolve()
TAG_FONT_FOLDER = Path("fonts").resolve()

WIDTH = 1500
HEIGHT = 500
BORDER = 0

CENTERX = round(WIDTH / 2)
CENTERY = round(HEIGHT / 2)


def background() -> svg.Rect:
    background = svg.Rect(
        x=0,
        y=0,
        width=WIDTH,
        height=HEIGHT,
        fill="white",
    )

    return background


def add_new_tag() -> svg.Element:
    fonts = [
        "graffiti youth",
        "graffiti city",
        "shock graffiti",
    ]

    # https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorials/SVG_from_scratch/Paths

    name = "Bert Plasschaert"
    width = 400
    segment_count = randrange(1, round(len(name) / 3), 1)
    segment_width = int(width / segment_count)

    segments: list[svg.ArcRel] = []
    for i in range(segment_count):
        segments.append(
            svg.ArcRel(
                dx=segment_width,  # end x
                dy=0,  # end y
                rx=randrange(segment_width, segment_width * 2),  # radius x
                ry=randrange(segment_width, segment_width * 2),  # radius y
                angle=randrange(160, 240),  # rotatie tov x as
                large_arc=0,  # outer arc flag
                sweep=i % 2,  # sweep flag (inverse)
            )
        )

    path = svg.Path(
        id="test",
        # stroke="black",
        fill="transparent",
        d=[
            svg.M(
                x=CENTERX,
                y=CENTERY,
            ),
            *segments,
        ],
        transform=[svg.Rotate(randrange(-15, 15), CENTERX, CENTERY)],
    )

    textpath = svg.TextPath(
        text=name,
        href="#test",
        font_size=56,
        startOffset=20,
        font_family="graffiti youth",
        fill="purple",
    )
    text = svg.Text(elements=[textpath])

    # return path
    return svg.G(
        id="tag",
        elements=[
            path,
            text,
        ],
    )


def load_encoded_fonts() -> str:
    """
    Used the techinique from this article:
    https://blog.frankel.ch/fonts-embedded-svg/
    """

    encoded_fonts = []
    for font in TAG_FONT_FOLDER.iterdir():
        with open(font, "r", encoding="UTF-8") as f:
            encoded_fonts.append(f.read())

    return "\n".join(encoded_fonts)


def draw() -> svg.SVG:
    return svg.SVG(
        overflow="hidden",
        viewBox=svg.ViewBoxSpec(
            0,
            0,
            WIDTH,
            HEIGHT,
        ),
        elements=[
            background(),
            add_new_tag(),
            # title(),
            # tag_hint(),
            # svg.Style(text=load_encoded_fonts()),
        ],
    )


if __name__ == "__main__":
    with open(TARGET_FILE, "w", encoding="UTF-8") as f:
        result = draw()
        f.write(result.as_str())
