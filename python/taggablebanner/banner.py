# stdlib modules
import random
import logging
from pathlib import Path
from xml.dom import minidom

# thirdparty modules
import svg

# tool modules
from taggablebanner.svgutils.safezones import SafeZone
from taggablebanner.svgutils.safezones import SafeZoneCircle
from taggablebanner.svgutils.safezones import SafeZoneSquare
from taggablebanner.svgutils.safezones import CanvasZone

from taggablebanner.svgutils.tag import Tag
from taggablebanner.svgutils.tag import build_tag
from taggablebanner.svgutils.tag import build_tag_from_minidom

from taggablebanner import const

logger = logging.getLogger(__name__)


def load_in_svg_component_from_file(file_name: str) -> str:
    """Load in SVG element snippet from file as string."""
    with open(Path(const.SVG_PARTS_FOLDER, file_name).with_suffix(".svg")) as f:
        return f.read()


def element_background() -> svg.G:
    """Construct background of banner."""
    background = svg.Rect(
        x=0,
        y=0,
        width=const.BANNER_WIDTH,
        height=const.BANNER_HEIGHT,
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
    """Construct the title of the banner."""

    title_front = svg.Text(
        text="Hello!",
        font_family="crysh graffiti regular",
        font_size=200,
        text_anchor="middle",
        class_="title",
        x=const.BANNER_CENTER_X,
        y=const.BANNER_CENTER_Y + 60,
    )

    title_back = svg.Text(
        text="Hello!",
        font_family="crysh graffiti extrude",
        font_size=200,
        text_anchor="middle",
        class_="title_back",
        x=const.BANNER_CENTER_X,
        y=const.BANNER_CENTER_Y + 60,
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
    """Construct the add tag button of the banner."""
    arrow = svg.G(
        text=load_in_svg_component_from_file("arrow_01"),
        transform=[
            svg.Rotate(-5, 20, const.BANNER_HEIGHT - 100),
            svg.Translate(15, const.BANNER_HEIGHT - 45),
            svg.Scale(1.5, 1.5),
        ],
    )
    hint = svg.Text(
        text="Add your tag!",
        font_family="graffiti city",
        font_size=32,
        class_="hint",
        x=45,
        y=const.BANNER_HEIGHT - 50,
        transform=svg.Rotate(5, 20, const.BANNER_HEIGHT - 100),
    )

    return svg.G(
        elements=[
            arrow,
            hint,
        ]
    )


def element_encoded_fonts() -> str:
    """
    Encode the custom fonts into style tags.

    Used the techinique from this article:
    https://blog.frankel.ch/fonts-embedded-svg/
    """
    encoded_fonts = []
    for font in const.FONT_FOLDER.iterdir():
        with open(font, "r", encoding="UTF-8") as f:
            encoded_fonts.append(f.read())

    return "\n".join(encoded_fonts)


def element_color_switcher() -> str:
    """Load the color presets into a style tag."""
    preset_color_classes = "\n".join([str(preset) for preset in const.COLOR_PRESETS])
    light_gradient_switch_values = "\n".join(
        [preset.gradient_light for preset in const.COLOR_PRESETS]
    )
    dark_gradient_switch_values = "\n".join(
        [preset.gradient_dark for preset in const.COLOR_PRESETS]
    )
    light_trigger = (
        f":root {{{light_gradient_switch_values};color-scheme: light dark;}}\n"
    )
    dark_trigger = f"@media (prefers-color-scheme: dark) {{:root {{\n{dark_gradient_switch_values}}}}}\n"
    return light_trigger + dark_trigger + preset_color_classes


def element_exclusionzones() -> list[SafeZone]:
    """Construct the tag exclusionzones."""
    sz_01 = SafeZoneCircle(cx=-0, cy=-110, r=240)
    sz_02 = SafeZoneCircle(cx=105, cy=const.BANNER_HEIGHT + 30, r=140)
    sz_03 = SafeZoneCircle(cx=440, cy=const.BANNER_HEIGHT + 30, r=140)
    sz_04 = SafeZoneCircle(
        cx=const.BANNER_WIDTH - 340, cy=const.BANNER_HEIGHT - 10, r=60
    )
    sz_05 = SafeZoneCircle(cx=const.BANNER_WIDTH, cy=const.BANNER_HEIGHT + 180, r=300)
    sz_06 = SafeZoneCircle(cx=const.BANNER_WIDTH, cy=-110, r=270)

    title_height = 200
    sz_title_01 = SafeZoneSquare(
        x=round(const.BANNER_CENTER_X - (title_height / 2) - title_height),
        y=round(const.BANNER_CENTER_Y - (title_height / 2)),
        width=title_height,
    )
    sz_title_02 = SafeZoneSquare(
        x=round(const.BANNER_CENTER_X - (title_height / 2)),
        y=round(const.BANNER_CENTER_Y - (title_height / 2)),
        width=title_height,
    )
    sz_title_03 = SafeZoneSquare(
        x=round(const.BANNER_CENTER_X - (title_height / 2) + title_height),
        y=round(const.BANNER_CENTER_Y - (title_height / 2)),
        width=title_height,
    )

    return [
        sz_01,
        sz_02,
        sz_03,
        sz_04,
        sz_05,
        sz_06,
        sz_title_01,
        sz_title_02,
        sz_title_03,
    ]


def check_bbox_allowed(tag: Tag) -> bool:
    """Check if provided tag its position is allowed.

    This function will check if every boundingbox point of the provided
    tag is located outside of any exclusion zone and within the canvas.
    """
    for zone in element_exclusionzones():
        for point in tag.bbox_points_transformed:
            if zone.check_if_point_in(point[0], point[1]):
                return False

    # check if tag is fully in the canvas
    canvas_zone = CanvasZone(0, 0, const.BANNER_WIDTH, const.BANNER_HEIGHT)
    for point in tag.bbox_points_transformed:
        if not canvas_zone.check_if_point_in(point[0], point[1]):
            return False

    return True


def make_tag(text: str) -> Tag:
    """Construct an unvalidated tag object with the provided text."""
    picked_font = random.choice(const.FONTS)
    location_x = random.randrange(0, const.BANNER_WIDTH)
    location_y = random.randrange(0, const.BANNER_HEIGHT)
    color_preset = random.choice(const.TAG_COLOR_PRESETS)

    return build_tag(
        text=text,
        x=location_x,
        y=location_y,
        font=picked_font,
        color_class=color_preset.name,
    )


def element_tag(text: str) -> Tag:
    """Construct a valided tag with the provided text."""
    tag = make_tag(text)
    while not check_bbox_allowed(tag):
        tag = make_tag(text)

    return tag


def get_existing_tags() -> list[Tag]:
    """Extract the existing tags from the existing banner svg.

    The svg module has no support to read existing svg files into svg objects.
    This function uses the minidom xml module to extract the tag elements and
    manually construct them into Tag objects
    """
    if not const.BANNER_FILE.exists():
        return []

    with open(const.BANNER_FILE, "r", encoding="UTF-8") as f:
        doc: minidom.Document = minidom.parse(f)

    tags: list[Tag] = list()
    for element in doc.getElementsByTagName("g"):
        if element.getAttribute("id") != "tag":
            continue

        try:
            tags.append(build_tag_from_minidom(element))
        except IndexError:
            logger.error("malformed tag svg group, skipping...")
            continue

    return tags


def add_tag(text: str) -> svg.SVG:
    """Adds a tag with the provided text to the banner."""

    import string

    def random_name():
        size = random.randrange(6, 22)
        chars = string.ascii_uppercase + string.digits
        return "".join(random.choice(chars) for _ in range(size))

    tags = [element_tag(random_name()) for i in range(50)]
    element_tags = [t.element_group for t in tags]
    bbox_og = [t.bbox_points_element for t in tags]
    bbox_transformed = [t.bbox_points_transformed_element for t in tags]

    result = svg.SVG(
        overflow="hidden",
        viewBox=svg.ViewBoxSpec(
            0,
            0,
            const.BANNER_WIDTH,
            const.BANNER_HEIGHT,
        ),
        elements=[
            element_background(),
            *[tag.element_group for tag in get_existing_tags()],
            # *element_tags,
            # *bbox_og,
            # *bbox_transformed,
            element_tag(text).element_group,
            element_title(),
            element_button_hint(),
            # svg.G(elements=[sz.element for sz in element_exclusionzones()]),
            *[preset.gradient_elements for preset in const.COLOR_PRESETS],
            svg.Style(text=element_encoded_fonts()),
            svg.Style(text=element_color_switcher()),
        ],
    )

    with open(const.BANNER_FILE, "w") as f:
        f.write(result.as_str())


if __name__ == "__main__":
    from datetime import datetime

    add_tag(f"test-{datetime.now().timestamp()}")
