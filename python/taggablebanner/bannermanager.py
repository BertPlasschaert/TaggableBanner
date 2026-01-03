from pathlib import Path
import string
import random
from xml.dom import minidom

import svg

from svgutils.safezones import SafeZone
from svgutils.safezones import SafeZoneCircle
from svgutils.safezones import SafeZoneRect

from svgutils.fontbb import FontBB
from svgutils.colorpreset import ColorPreset
from svgutils.textbounded import TextBounded

SVG_PARTS_FOLDER = Path("svg_parts")
OUTPUT_FILE = Path("banner.svg")
FONT_FOLDER = Path("fonts")

WIDTH = 1500
HEIGHT = 500

CENTERX = round(WIDTH / 2)
CENTERY = round(HEIGHT / 2)

FONTS = [
    FontBB("graffiti youth", 0.7, 0.4),
    FontBB("graffiti city", 0.76, 0.43),
    FontBB("shock graffiti", 0.65, 0.39),
]

COLOR_PRESETS = [
    ColorPreset("title", "hsl(116,67%,66%)", "hsl(168,51%,53%)"),
    ColorPreset("title_back", "hsl(101,100%,27%)", "hsl(176,48%,29%)"),
    ColorPreset("hint", "hsl(321, 84%, 58%)", "hsl(112, 55%, 57%)"),
    ColorPreset("bricks", "hsl(0,0%,85%)", "hsl(216, 34%, 11%)"),
    ColorPreset("banner_background", "hsl(0,0%,95%)", "hsl(216,28%,7%)"),
    ColorPreset("tag_orange", "hsl(13,100%,59%)", "hsl(13,81%,18%)"),
    ColorPreset("tag_pink", "hsl(337,100%,63%)", "hsl(337,56%,27%)"),
    ColorPreset("tag_blue", "hsl(205,100%,60%)", "hsl(205,100%,25%)"),
    ColorPreset("tag_purple", "hsl(274,100%,72%)", "hsl(274,88%,23%)"),
    ColorPreset("tag_green", "hsl(118,88%,47%)", "hsl(118,83%,19%)"),
]
TAG_COLOR_PRESETS = list(filter(lambda p: (p.name.startswith("tag_")), COLOR_PRESETS))


def random_name():
    # TODO: remove later
    size = random.randrange(6, 22)
    chars = string.ascii_uppercase + string.digits
    return "".join(random.choice(chars) for _ in range(size))


def load_in_svg_component_from_file(file_name: str) -> str:
    with open(Path(SVG_PARTS_FOLDER, file_name).with_suffix(".svg")) as f:
        return f.read()


def element_background() -> svg.G:
    background = svg.Rect(
        x=0,
        y=0,
        width=WIDTH,
        height=HEIGHT,
        class_="banner_background",
    )

    bricks_01 = svg.G(
        transform=[
            svg.Translate(-20, -35),
            svg.Scale(0.2, 0.2),
        ],
        text=load_in_svg_component_from_file("bricks_01"),
    )
    bricks_02 = svg.G(
        transform=[
            svg.Rotate(180),
            svg.Translate(-1598, -284),
            svg.Scale(0.2, 0.2),
        ],
        text=load_in_svg_component_from_file("bricks_02"),
    )
    bricks_03 = svg.G(
        transform=[
            svg.Translate(240, 250),
            svg.Scale(0.2, 0.2),
        ],
        text=load_in_svg_component_from_file("bricks_03"),
    )
    bricks_04 = svg.G(
        transform=[
            svg.Translate(1100, 250),
            svg.Scale(0.2, 0.2),
        ],
        text=load_in_svg_component_from_file("bricks_04"),
    )
    crack_01 = svg.G(
        transform=[
            svg.Translate(970, 400),
            svg.Scale(0.8, 0.8),
        ],
        text=load_in_svg_component_from_file("crack_01"),
    )
    crack_02 = svg.G(
        transform=[
            svg.Translate(420, 80),
            svg.Scale(0.8, 0.8),
        ],
        text=load_in_svg_component_from_file("crack_02"),
    )
    return svg.G(
        elements=[
            background,
            bricks_01,
            bricks_02,
            bricks_03,
            bricks_04,
            crack_01,
            crack_02,
        ]
    )


def element_title() -> svg.G:
    title_front = svg.Text(
        text="Hello!",
        font_family="crysh graffiti regular",
        font_size=200,
        text_anchor="middle",
        class_="title",
        x=CENTERX,
        y=CENTERY + 60,
    )
    title_back = svg.Text(
        text="Hello!",
        font_family="crysh graffiti extrude",
        font_size=200,
        text_anchor="middle",
        class_="title_back",
        x=CENTERX,
        y=CENTERY + 60,
    )
    splat_01 = svg.G(
        transform=[
            svg.Translate(855, 220),
            svg.Scale(2, 2),
        ],
        text=load_in_svg_component_from_file("splat_01"),
    )
    splat_02 = svg.G(
        transform=[
            svg.Translate(450, 240),
            svg.Scale(1.5, 1.5),
        ],
        text=load_in_svg_component_from_file("splat_02"),
    )

    return svg.G(
        elements=[
            splat_01,
            splat_02,
            title_back,
            title_front,
        ]
    )


def element_button_hint() -> svg.G:
    arrow = svg.G(
        text=load_in_svg_component_from_file("arrow_01"),
        transform=[
            svg.Rotate(5, 20, HEIGHT - 100),
            svg.Translate(30, HEIGHT - 50),
            svg.Scale(1.5, 1.5),
        ],
    )
    hint = svg.Text(
        text="Add your tag!",
        font_family="graffiti city",
        font_size=32,
        class_="hint",
        x=45,
        y=HEIGHT - 50,
        transform=svg.Rotate(5, 20, HEIGHT - 100),
    )

    return svg.G(
        elements=[
            arrow,
            hint,
        ]
    )


def element_encoded_fonts() -> str:
    """
    Used the techinique from this article:
    https://blog.frankel.ch/fonts-embedded-svg/
    """

    encoded_fonts = []
    for font in FONT_FOLDER.iterdir():
        with open(font, "r", encoding="UTF-8") as f:
            encoded_fonts.append(f.read())

    return "\n".join(encoded_fonts)


def element_color_switcher() -> str:
    preset_color_classes = "\n".join([str(preset) for preset in COLOR_PRESETS])
    global_trigger = ":root {color-scheme: light dark;}\n"
    return global_trigger + preset_color_classes


def element_inclusionzones() -> list[SafeZone]:
    sz_01 = SafeZoneRect(
        x=0,
        y=0,
        width=WIDTH,
        height=HEIGHT,
    )

    return [sz_01]


def element_exclusionzones() -> list[SafeZone]:
    sz_01 = SafeZoneCircle(cx=-0, cy=-110, r=240)
    sz_02 = SafeZoneCircle(cx=105, cy=HEIGHT + 30, r=140)
    sz_03 = SafeZoneCircle(cx=440, cy=HEIGHT + 30, r=140)
    sz_04 = SafeZoneCircle(cx=WIDTH - 340, cy=HEIGHT - 10, r=60)
    sz_05 = SafeZoneCircle(cx=WIDTH, cy=HEIGHT + 180, r=300)
    sz_06 = SafeZoneCircle(cx=WIDTH, cy=-110, r=270)

    title_bb = (540, 220)
    sz_title = SafeZoneRect(
        x=CENTERX - (title_bb[0] / 2),
        y=CENTERY - (title_bb[1] / 2),
        width=title_bb[0],
        height=title_bb[1],
    )

    return [
        sz_01,
        sz_02,
        sz_03,
        sz_04,
        sz_05,
        sz_06,
        sz_title,
    ]


def check_bbox_allowed(bbox) -> bool:
    for zone in element_exclusionzones():
        for point in bbox.points_bbox:
            if zone.check_if_point_in(point[0], point[1]):
                return False

    for zone in element_inclusionzones():
        for point in bbox.points_bbox:
            if not zone.check_if_point_in(point[0], point[1]):
                return False

    return True


def make_tag(text: str) -> TextBounded:
    picked_font = random.choice(FONTS)

    location_x = random.randrange(0, WIDTH)
    location_y = random.randrange(0, HEIGHT)

    rotation = random.randrange(-15, 15)
    # TODO: fix rotation bb calculation
    # https://www.cs.usfca.edu/~galles/visualization/RotateTranslate2D.html
    # rotation = 0

    color_preset = random.choice(TAG_COLOR_PRESETS)
    font_size = max(64 - (len(text) * 2.5), 24)
    return TextBounded(
        text=text,
        x=location_x,
        y=location_y,
        rotation=rotation,
        font=picked_font,
        font_size=font_size,
        color_class=color_preset.name,
    )


def element_tag(name: str) -> svg.Element:
    tag = make_tag(name)
    invalid_location = True
    while invalid_location:
        if not check_bbox_allowed(tag):
            tag = make_tag(name)
            continue

        invalid_location = False

    return svg.G(
        elements=[
            tag.element_text,
            # tag.element_bbox,
        ]
    )


def minidom_to_tag(minidom_element: minidom.Element) -> TextBounded:
    font_family = minidom_element.getAttribute("font-family")
    font = [font for font in FONTS if font.name == font_family][0]

    transform = minidom_element.getAttribute("transform")
    rotation_degrees = transform.split("(")[1].split(" ")[0]

    return TextBounded(
        text=minidom_element.firstChild.nodeValue,
        x=int(minidom_element.getAttribute("x")),
        y=int(minidom_element.getAttribute("y")),
        rotation=int(rotation_degrees),
        font=font,
        font_size=int(float(minidom_element.getAttribute("font-size"))),
        color_class=minidom_element.getAttribute("class"),
    )


def get_existing_tags() -> list[TextBounded]:
    if not OUTPUT_FILE.exists():
        return []

    with open(OUTPUT_FILE, "r", encoding="UTF-8") as svg_file:
        doc = minidom.parse(svg_file)

    elements_text: list[minidom.Element] = [
        path for path in doc.getElementsByTagName("text")
    ]

    tag_groups: list[svg.G] = list()
    for e in elements_text:
        if e.getAttribute("id") != "tag":
            continue

        tag = minidom_to_tag(e)
        tag_groups.append(
            svg.G(
                elements=[
                    tag.element_text,
                    # tag.element_bbox,
                ]
            )
        )

    return tag_groups


def add_tag(text: str) -> svg.SVG:
    tags = [element_tag(random_name()) for i in range(50)]

    result = svg.SVG(
        overflow="hidden",
        viewBox=svg.ViewBoxSpec(
            0,
            0,
            WIDTH,
            HEIGHT,
        ),
        elements=[
            element_background(),
            get_existing_tags(),
            # *tags,
            element_tag(text),
            element_title(),
            element_button_hint(),
            # svg.G(elements=[sz.element for sz in element_exclusionzones()]),
            # svg.G(elements=[sz.element for sz in element_inclusionzones()]),
            svg.Style(text=element_encoded_fonts()),
            svg.Style(text=element_color_switcher()),
        ],
    )

    with open(OUTPUT_FILE, "w") as f:
        f.write(result.as_str())
