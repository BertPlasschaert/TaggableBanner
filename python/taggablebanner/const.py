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
