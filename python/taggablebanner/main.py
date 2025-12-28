from pathlib import Path
from random import randrange
from random import choice
import math
from xml.dom import minidom
import svg

TARGET_FILE = Path("banner.svg").resolve()
TAG_FONT_FOLDER = Path("fonts").resolve()

WIDTH = 1500
HEIGHT = 500
BORDER = 0

CENTERX = round(WIDTH / 2)
CENTERY = round(HEIGHT / 2)


def check_in_circular_safezone(point, center, r):
    distance = math.dist(center, point)
    if distance <= r:
        return True


def title() -> svg.Element:
    hello = svg.Text(
        id="hello",
        text="Hello!",
        font_family="crysh graffiti regular",
        font_size=124,
        text_anchor="middle",
        fill="hsl(112, 55%, 57%)",
        x="50%",
        y=CENTERY + 20,
    )

    hello_extrude = svg.Text(
        id="hello",
        text="Hello!",
        font_family="crysh graffiti extrude",
        font_size=124,
        text_anchor="middle",
        fill="hsl(176, 48%, 29%)",
        x="50%",
        y=CENTERY + 20,
    )

    title_group = svg.G(
        elements=[
            hello_extrude,
            hello,
        ],
    )

    return title_group


def tag_hint() -> svg.Element:
    hint = svg.Text(
        text="Add your tag!",
        font_family="graffiti city",
        font_size=32,
        fill="hsl(112, 55%, 57%)",
        x=45,
        y=HEIGHT - 50,
        transform=svg.Rotate(5, 20, HEIGHT - 100),
    )

    arrow_path_r = [
        svg.M(9.359, 103.53),
        svg.C(18.54, 98.073, 28.294, 93.971, 38.224, 90.092),
        svg.C(47.621, 86.42, 59.555, 82.184, 66.782, 74.97),
        svg.C(68.218, 73.538, 66.88, 71.206, 64.94, 71.568),
        svg.C(55.542, 73.32, 46.351, 78.442, 37.433, 81.866),
        svg.C(26.592, 86.028, 16.012, 91.552, 6.369, 98.005),
        svg.C(3.06, 100.219, 5.83, 105.626, 9.359, 103.530),
        svg.Z(),
    ]

    arrow_path_l = [
        svg.M(9.668, 101.695),
        svg.C(10.467, 89.364, 10.79, 77.012, 11.886, 64.695),
        svg.C(12.852, 53.796, 15.235, 41.624, 12.166, 30.909),
        svg.C(11.564, 28.811, 8.163, 27.672, 7.058, 30.089),
        svg.C(2.317, 40.477, 1.607, 53.085, 0.679, 64.329),
        svg.C(-0.373, 77.076, -0.631, 89.998, 3.124, 102.335),
        svg.C(4.209, 105.902, 9.417, 105.545, 9.668, 101.695),
        svg.Z(),
    ]

    arrow_r = svg.Path(
        d=arrow_path_r,
        fill="hsl(112, 55%, 57%)",
    )
    arrow_l = svg.Path(
        d=arrow_path_l,
        fill="hsl(112, 55%, 57%)",
    )

    arrow_01 = svg.G(
        elements=[
            arrow_l,
            arrow_r,
        ],
        transform=[svg.Translate(20, HEIGHT - 50), svg.Scale(0.4, 0.4)],
    )
    arrow_02 = svg.G(
        elements=[
            arrow_l,
            arrow_r,
        ],
        transform=[svg.Translate(28, HEIGHT - 60), svg.Scale(0.38, 0.38)],
    )

    safe_zone = svg.Circle(
        cx=60,
        cy=HEIGHT + 20,
        r=200,
        fill="red",
    )

    hint_group = svg.G(
        elements=[
            # safe_zone,
            hint,
            arrow_01,
            arrow_02,
        ],
    )
    return hint_group


def background() -> svg.Element:
    background = svg.Rect(
        width="100%",
        height="100%",
        fill="hsl(214, 25%, 11%)",
        stroke="hsl(214, 12%, 27%)",
        stroke_width=2,
    )

    return background


def add_new_tag(name: str) -> svg.Element:
    safe_zone = svg.Circle(
        cx=CENTERX - 60,
        cy=CENTERY,
        r=200,
        fill="red",
    )

    location_x = randrange(-10, WIDTH - 50, 1)
    location_y = randrange(40, HEIGHT, 1)

    while check_in_circular_safezone(
        [location_x, location_y], [CENTERX - 60, CENTERY], 200
    ) or check_in_circular_safezone([location_x, location_y], [60, HEIGHT + 20], 200):
        location_x = randrange(-10, WIDTH - 50, 1)
        location_y = randrange(40, HEIGHT, 1)

    rotation = randrange(-30, 30)
    hue = randrange(-360, 360, 1)
    font_size = randrange(32, 52)

    fonts = [
        "graffiti youth",
        "graffiti city",
        "shock graffiti",
    ]

    name = svg.Text(
        id="tag",
        text=f"{name}",
        font_family=choice(fonts),
        x=location_x,
        y=location_y,
        text_anchor="center",
        font_size=font_size,
        fill=f"hsl({hue}, 55%, 57%)",
        # stroke="hsl(214, 25%, 11%)",
        stroke=f"hsl({hue}, 85%, 37%)",
        stroke_width=1.5,
        transform=svg.Rotate(
            rotation,
            location_x,
            location_y,
        ),
    )

    # return safe_zone
    return name


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


def draw(new_name: str) -> svg.SVG:
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
            get_existing_tags(),
            add_new_tag(new_name),
            title(),
            tag_hint(),
            svg.Style(text=load_encoded_fonts()),
        ],
    )


def minidom_to_svg(minidom_element: minidom.Element) -> svg.Element:
    return svg.Text(
        id="tag",
        text=minidom_element.firstChild.nodeValue,
        font_family=minidom_element.getAttribute("font-family"),
        x=minidom_element.getAttribute("x"),
        y=minidom_element.getAttribute("y"),
        text_anchor="center",
        font_size=minidom_element.getAttribute("font-size"),
        fill=minidom_element.getAttribute("fill"),
        transform=minidom_element.getAttribute("transform"),
        stroke=minidom_element.getAttribute("stroke"),
        stroke_width=minidom_element.getAttribute("stroke-width"),
    )


def get_existing_tags() -> list[svg.Text]:
    if not TARGET_FILE.exists():
        return list()

    with open(TARGET_FILE, "r", encoding="UTF-8") as svg_file:
        doc = minidom.parse(svg_file)

    elements_text: list[minidom.Element] = [
        path for path in doc.getElementsByTagName("text")
    ]

    elements_tag: list[svg.Text] = list()
    for e in elements_text:
        if e.getAttribute("id") != "tag":
            continue

        elements_tag.append(minidom_to_svg(e))

    return elements_tag


if __name__ == "__main__":
    for i in range(20):
        result = draw(new_name=f"Bert{i}")

        with open(TARGET_FILE, "w", encoding="UTF-8") as f:
            f.write(result.as_str())
