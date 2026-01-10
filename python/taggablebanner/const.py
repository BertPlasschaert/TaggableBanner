from pathlib import Path

from svgutils.fontbb import FontBB
from svgutils.colorpreset import ColorPreset

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
    ColorPreset(
        "title",
        fill_light="hsl(116,67%,66%)",
        fill_dark="hsl(168,51%,53%)",
    ),
    ColorPreset(
        "title_back",
        fill_light="hsl(101,100%,27%)",
        fill_dark="hsl(176,48%,29%)",
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
        "tag_orange",
        fill_light="hsl(13,100%,59%)",
        fill_dark="hsl(13,81%,18%)",
        stroke_light="hsl(13,100%,69%)",
        stroke_dark="hsl(13,81%,8%)",
    ),
    ColorPreset(
        "tag_pink",
        fill_light="hsl(337,100%,63%)",
        fill_dark="hsl(337,56%,27%)",
        stroke_light="hsl(337,100%,73%)",
        stroke_dark="hsl(337,56%,7%)",
    ),
    ColorPreset(
        "tag_blue",
        fill_light="hsl(205,100%,60%)",
        fill_dark="hsl(205,100%,25%)",
        stroke_light="hsl(205,100%,70%)",
        stroke_dark="hsl(205,100%,15%)",
    ),
    ColorPreset(
        "tag_purple",
        fill_light="hsl(274,100%,72%)",
        fill_dark="hsl(274,88%,23%)",
        stroke_light="hsl(274,100%,82%)",
        stroke_dark="hsl(274,88%,13%)",
    ),
    ColorPreset(
        "tag_green",
        fill_light="hsl(118,88%,47%)",
        fill_dark="hsl(118,83%,19%)",
        stroke_light="hsl(118,88%,57%)",
        stroke_dark="hsl(118,83%,9%)",
    ),
]

TAG_COLOR_PRESETS = list(filter(lambda p: (p.name.startswith("tag_")), COLOR_PRESETS))
