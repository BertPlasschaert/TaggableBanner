# stdlib modules
from pathlib import Path

# tool modules
from taggablebanner.svgutils.fontbb import FontBB
from taggablebanner.svgutils.colorpreset import ColorPreset

BANNER_FILE = Path("banner.svg")
MD_FILE = Path("README.md")
SVG_PARTS_FOLDER = Path("svg_parts")

MD_START_MARKER = "<!--begin usernames-->\n"
MD_END_MARKER = "<!--end usernames-->\n"

BANNER_WIDTH = 1500
BANNER_HEIGHT = 500

BANNER_CENTER_X = round(BANNER_WIDTH / 2)
BANNER_CENTER_Y = round(BANNER_HEIGHT / 2)

FONT_FOLDER = Path("fonts")
FONTS = [
    FontBB("graffiti youth", 0.7, 0.4),
    FontBB("graffiti city", 0.76, 0.43),
    FontBB("shock graffiti", 0.65, 0.39),
]

gh_colors = {
    "gray": {
        0: "#f6f8fa",
        1: "#eaeef2",
        2: "#d0d7de",
        3: "#afb8c1",
        4: "#8c959f",
        5: "#6e7781",
        6: "#57606a",
        7: "#424a53",
        8: "#32383f",
        9: "#24292f",
    },
    "blue": {
        0: "#ddf4ff",
        1: "#b6e3ff",
        2: "#80ccff",
        3: "#54aeff",
        4: "#218bff",
        5: "#0969da",
        6: "#0550ae",
        7: "#033d8b",
        8: "#0a3069",
        9: "#002155",
    },
    "green": {
        0: "#dafbe1",
        1: "#aceebb",
        2: "#6fdd8b",
        3: "#4ac26b",
        4: "#2da44e",
        5: "#1a7f37",
        6: "#116329",
        7: "#044f1e",
        8: "#003d16",
        9: "#002d11",
    },
    "yellow": {
        0: "#fff8c5",
        1: "#fae17d",
        2: "#eac54f",
        3: "#d4a72c",
        4: "#bf8700",
        5: "#9a6700",
        6: "#7d4e00",
        7: "#633c01",
        8: "#4d2d00",
        9: "#3b2300",
    },
    "orange": {
        0: "#fff1e5",
        1: "#ffd8b5",
        2: "#ffb77c",
        3: "#fb8f44",
        4: "#e16f24",
        5: "#bc4c00",
        6: "#953800",
        7: "#762c00",
        8: "#5c2200",
        9: "#471700",
    },
    "red": {
        0: "#ffebe9",
        1: "#ffcecb",
        2: "#ffaba8",
        3: "#ff8182",
        4: "#fa4549",
        5: "#cf222e",
        6: "#a40e26",
        7: "#82071e",
        8: "#660018",
        9: "#4c0014",
    },
    "purple": {
        0: "#fbefff",
        1: "#ecd8ff",
        2: "#d8b9ff",
        3: "#c297ff",
        4: "#a475f9",
        5: "#8250df",
        6: "#6639ba",
        7: "#512a97",
        8: "#3e1f79",
        9: "#2e1461",
    },
    "pink": {
        0: "#ffeff7",
        1: "#ffd3eb",
        2: "#ffadda",
        3: "#ff80c8",
        4: "#e85aad",
        5: "#bf3989",
        6: "#99286e",
        7: "#772057",
        8: "#611347",
        9: "#4d0336",
    },
    "coral": {
        0: "#fff0eb",
        1: "#ffd6cc",
        2: "#ffb4a1",
        3: "#fd8c73",
        4: "#ec6547",
        5: "#c4432b",
        6: "#9e2f1c",
        7: "#801f0f",
        8: "#691105",
        9: "#510901",
    },
    "lemon": {
        0: "#FDF5B3",
        1: "#F4E162",
        2: "#DEC741",
        3: "#C5AA20",
        4: "#A88D02",
        5: "#866D00",
        6: "#685400",
        7: "#534100",
        8: "#413200",
        9: "#322400",
    },
    "lime": {
        0: "#EAFABA",
        1: "#CDEC78",
        2: "#B1D353",
        3: "#94B83B",
        4: "#799A2A",
        5: "#5A791B",
        6: "#425E13",
        7: "#2F4A06",
        8: "#233B03",
        9: "#182C01",
    },
    "teal": {
        0: "#DAF9F5",
        1: "#B0EAE3",
        2: "#6BD6D0",
        3: "#49BCB7",
        4: "#339D9B",
        5: "#197B7B",
        6: "#136061",
        7: "#024B4D",
        8: "#063A3C",
        9: "#052B2C",
    },
    "indigo": {
        0: "#EFF2FF",
        1: "#D7DDFF",
        2: "#B9C2FF",
        3: "#9AA4FF",
        4: "#7683FF",
        5: "#545DF0",
        6: "#3C42D0",
        7: "#2C33A5",
        8: "#22297F",
        9: "#191F5C",
    },
}


# https://primer.style/brand/primitives/color/
dark_fill_color_codes = [
    "#0c2d6b",  # blue 8
    "#196c2e",  # green 6
    "#8C7600",  # yellow 5
    "#8e1519",  # red 7
    "#9e3670",  # pink 6
    "#3c1e70",  # purple 8
]

light_fill_color_codes = [
    "#",  # blue
    "#",  # green
    "#",  # yellow
    "#",  # red
    "#",  # pink
    "#",  # purple
]

_lighter_stroke_color_codes = [
    "#388bfd",  # blue 4
    "#56d364",  # green 2
    "#e3b341",  # yellow 2
    "#da3633",  # red 5
    "#f778ba",  # pink 3
    "#a371f7",  # purple 4
]

_darker_stroke_color_codes = [
    "#051d4d",  # blue 9
    "#033a16",  # green 8
    "#693e00",  # yellow 7
    "#67060c",  # red 8
    "#5e103e",  # pink 8
    "#271052",  # purple 9
]

stroke_dark = _darker_stroke_color_codes


COLOR_PRESETS = [
    ColorPreset(
        "title",
        # fill_light=gh_colors["coral"][4],
        fill_light="linear-gradient(90deg,rgba(42, 123, 155, 1) 0%, rgba(87, 199, 133, 1) 50%, rgba(237, 221, 83, 1) 100%);",
        fill_dark="#56d364",
        # fill_light="#7ee787",
        # fill_dark="#7ee787",
    ),
    ColorPreset(
        "title_back",
        fill_light=gh_colors["coral"][5],
        fill_dark="#196c2e",
    ),
    ColorPreset(
        "hint",
        fill_light="hsl(321, 84%, 58%)",
        fill_dark="hsl(112, 55%, 57%)",
    ),
    ColorPreset(
        "bricks",
        fill_light="hsl(0,0%,85%)",
        fill_dark="hsl(216, 34%, 11%)",
    ),
    ColorPreset(
        "banner_background",
        fill_light="hsl(0,0%,95%)",
        fill_dark="hsl(216,28%,7%)",
    ),
    ColorPreset(
        "tag_blue",
        fill_dark=gh_colors["blue"][8],
        fill_light=gh_colors["blue"][2],
        stroke_dark=gh_colors["blue"][9],
        stroke_light=gh_colors["blue"][1],
    ),
    ColorPreset(
        "tag_green",
        fill_dark=gh_colors["green"][6],
        fill_light=gh_colors["green"][2],
        stroke_dark=gh_colors["green"][6],
        stroke_light=gh_colors["green"][2],
    ),
    ColorPreset(
        "tag_yellow",
        fill_dark=gh_colors["yellow"][5],
        fill_light=gh_colors["yellow"][1],
        stroke_dark=gh_colors["yellow"][7],
        stroke_light=gh_colors["yellow"][0],
    ),
    ColorPreset(
        "tag_red",
        fill_dark=gh_colors["red"][7],
        fill_light=gh_colors["red"][3],
        stroke_dark=gh_colors["red"][8],
        stroke_light=gh_colors["red"][3],
    ),
    ColorPreset(
        "tag_pink",
        fill_dark=gh_colors["pink"][6],
        fill_light=gh_colors["pink"][2],
        stroke_dark=gh_colors["pink"][8],
        stroke_light=gh_colors["pink"][1],
    ),
    ColorPreset(
        "tag_purple",
        fill_dark=gh_colors["purple"][8],
        fill_light=gh_colors["purple"][3],
        stroke_dark=gh_colors["purple"][9],
        stroke_light=gh_colors["purple"][2],
    ),
]

TAG_COLOR_PRESETS = list(filter(lambda p: (p.name.startswith("tag_")), COLOR_PRESETS))
