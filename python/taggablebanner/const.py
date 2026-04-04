# stdlib modules
import os
import json
from pathlib import Path

# tool modules
from taggablebanner.svgutils.fontbb import FontBB
from taggablebanner.svgutils.colorpreset import ColorPreset


from pathlib import Path


def get_latest_banner_file(directory: Path):
    def get_creation_time(item):
        return item.stat().st_ctime

    items = list(directory.glob("banner*.svg"))
    if not items:
        return Path(directory, "banner.svg")
    sorted_items = sorted(items, key=get_creation_time)
    return sorted_items[-1]


# NOTE: set optional custom folder root via environment variable
TARGET_FOLDER = Path(os.environ.get("TAGGABLE_BANNER_ROOT", ""))

BANNER_FILE = get_latest_banner_file(TARGET_FOLDER)
MD_FILE = Path(TARGET_FOLDER, Path("README.md"))

MODULE_ROOT = Path(__file__).parent
RESOURCES_FOLDER = Path(MODULE_ROOT, Path("resources"))
SVG_PARTS_FOLDER = Path(RESOURCES_FOLDER, Path("svg_parts"))
FONT_FOLDER = Path(RESOURCES_FOLDER, Path("fonts"))

MD_START_MARKER = "<!--begin usernames-->\n"
MD_END_MARKER = "<!--end usernames-->\n"

BANNER_WIDTH = 1500
BANNER_HEIGHT = 500

BANNER_CENTER_X = round(BANNER_WIDTH / 2)
BANNER_CENTER_Y = round(BANNER_HEIGHT / 2)

FONTS = [
    FontBB("graffiti youth", 0.7, 0.4),
    FontBB("graffiti city", 0.76, 0.43),
    FontBB("shock graffiti", 0.65, 0.39),
]


# NOTE: Github color palette in json format, colors used from:
# https://primer.style/brand/primitives/color/
with open(Path(RESOURCES_FOLDER, Path("github_colors.json"))) as f:
    gh_colors = json.load(f)

COLOR_PRESETS = [
    ColorPreset(
        "title",
        fill_light_start=gh_colors["lime"]["1"],
        fill_light_stop=gh_colors["lime"]["3"],
        fill_dark_start=gh_colors["coral"]["6"],
        fill_dark_stop=gh_colors["coral"]["9"],
    ),
    ColorPreset(
        "title_back",
        fill_light_start=gh_colors["lime"]["3"],
        fill_light_stop=gh_colors["lime"]["3"],
        fill_dark_start=gh_colors["coral"]["9"],
        fill_dark_stop=gh_colors["coral"]["9"],
    ),
    ColorPreset(
        "hint",
        fill_light_start="GreenYellow",
        fill_light_stop="LawnGreen",
        fill_dark_start=gh_colors["green"]["3"],
        fill_dark_stop=gh_colors["green"]["4"],
        glow_dark=gh_colors["green"]["8"],
    ),
    ColorPreset(
        "bricks",
        fill_light_start="hsl(0,0%,85%)",
        fill_light_stop="hsl(0,0%,85%)",
        fill_dark_start="hsl(216, 34%, 11%)",
        fill_dark_stop="hsl(216, 34%, 11%)",
    ),
    ColorPreset(
        "banner_background",
        fill_light_start="hsl(0,0%,95%)",
        fill_light_stop="hsl(0,0%,95%)",
        fill_dark_start="hsl(216,28%,7%)",
        fill_dark_stop="hsl(216,28%,7%)",
    ),
    ColorPreset(
        "tag-blue",
        fill_light_start=gh_colors["blue"]["1"],
        fill_light_stop=gh_colors["pink"]["3"],
        fill_dark_start=gh_colors["blue"]["7"],
        fill_dark_stop=gh_colors["pink"]["7"],
        glow_dark=gh_colors["purple"]["9"],
        glow_light=gh_colors["pink"]["2"],
    ),
    ColorPreset(
        "tag-green",
        fill_light_start=gh_colors["green"]["3"],
        fill_light_stop=gh_colors["orange"]["2"],
        fill_dark_start=gh_colors["green"]["6"],
        fill_dark_stop=gh_colors["orange"]["6"],
        glow_dark=gh_colors["orange"]["8"],
        glow_light=gh_colors["yellow"]["2"],
    ),
    ColorPreset(
        "tag-yellow",
        fill_light_start=gh_colors["yellow"]["2"],
        fill_light_stop=gh_colors["blue"]["3"],
        fill_dark_start=gh_colors["yellow"]["7"],
        fill_dark_stop=gh_colors["blue"]["7"],
        glow_dark=gh_colors["blue"]["8"],
        glow_light=gh_colors["blue"]["1"],
    ),
    ColorPreset(
        "tag-red",
        fill_light_start=gh_colors["purple"]["2"],
        fill_light_stop=gh_colors["red"]["4"],
        fill_dark_start=gh_colors["purple"]["7"],
        fill_dark_stop=gh_colors["red"]["7"],
        glow_dark=gh_colors["red"]["8"],
        glow_light=gh_colors["red"]["2"],
    ),
    ColorPreset(
        "tag-pink",
        fill_light_start=gh_colors["pink"]["2"],
        fill_light_stop=gh_colors["green"]["2"],
        fill_dark_start=gh_colors["pink"]["7"],
        fill_dark_stop=gh_colors["green"]["7"],
        glow_dark=gh_colors["green"]["8"],
        glow_light=gh_colors["green"]["1"],
    ),
    ColorPreset(
        "tag-purple",
        fill_light_start=gh_colors["purple"]["2"],
        fill_light_stop=gh_colors["yellow"]["3"],
        fill_dark_start=gh_colors["purple"]["7"],
        fill_dark_stop=gh_colors["yellow"]["7"],
        glow_dark=gh_colors["yellow"]["8"],
        glow_light=gh_colors["coral"]["1"],
    ),
]

TAG_COLOR_PRESETS = list(filter(lambda p: (p.name.startswith("tag-")), COLOR_PRESETS))
