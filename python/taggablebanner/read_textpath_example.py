from pathlib import Path
from random import randrange
from random import choice
import math
from xml.dom import minidom
import svg
from svgutils.fontbb import FontBB

TARGET_FILE = Path("out_tmp.svg").resolve()
INPUT_FILE = Path("tmp.svg").resolve()
TAG_FONT_FOLDER = Path("fonts").resolve()

WIDTH = 1500
HEIGHT = 500
BORDER = 0

CENTERX = round(WIDTH / 2)
CENTERY = round(HEIGHT / 2)

FONTS = [
    FontBB("graffiti youth", 0.7, 0.4),
    FontBB("graffiti city", 0.76, 0.43),
    FontBB("shock graffiti", 0.65, 0.39),
]


def minidom_to_tag(minidom_element: minidom.Element):
    font_family = minidom_element.getAttribute("font-family")
    font = [font for font in FONTS if font.name == font_family][0]

    transform = minidom_element.getAttribute("transform")
    rotation_degrees = transform.split("(")[1].split(" ")[0]


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
        elements=[
            path,
            text,
        ]
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
            rebuild_existing_tags()
            # title(),
            # tag_hint(),
            # svg.Style(text=load_encoded_fonts()),
        ],
    )


def tag_from_minidom(minidom_tag_group: minidom.Element):
    path = [e for e in minidom_tag_group.childNodes if e.tagName == "path"][0]
    textpath = [
        e.childNodes[0] for e in minidom_tag_group.childNodes if e.tagName == "text"
    ][0]

    font_family = textpath.getAttribute("font-family")
    font = [font for font in FONTS if font.name == font_family][0]

    transform = path.getAttribute("transform")
    rotation_degrees = transform.split("(")[1].split(" ")[0]

    name = textpath.firstChild.nodeValue

    x = int(path.getAttribute("d").split(" ")[1])
    y = int(path.getAttribute("d").split(" ")[2])

    path = svg.Path(
        id=path.getAttribute("id"),
        fill="transparent",
        d=path.getAttribute("d"),
        transform=[svg.Rotate(rotation_degrees, x, y)],
    )

    textpath = svg.TextPath(
        text=name,
        href=textpath.getAttribute("href"),
        font_size=int(textpath.getAttribute("font-size")),
        startOffset=int(textpath.getAttribute("startOffset")),
        font_family=font_family,
        fill=textpath.getAttribute("fill"),
    )

    text = svg.Text(elements=[textpath])

    return svg.G(
        id="tag",
        elements=[
            path,
            text,
        ],
    )


def rebuild_existing_tags():
    with open(INPUT_FILE, "r", encoding="UTF-8") as f:
        doc: minidom.Document = minidom.parse(f)

    tags = list()
    groups: list[minidom.Element] = doc.getElementsByTagName("g")
    for element in groups:
        if element.getAttribute("id") != "tag":
            continue

        try:
            tags.append(tag_from_minidom(element))
        except IndexError:
            print("malformed tag svg group")
            continue

    return tags


if __name__ == "__main__":
    with open(TARGET_FILE, "w", encoding="UTF-8") as f:
        result = draw()
        f.write(result.as_str())
