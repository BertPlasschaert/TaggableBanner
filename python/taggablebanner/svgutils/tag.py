from dataclasses import dataclass
from xml.dom import minidom
import random

import svg

from taggablebanner.svgutils.fontbb import FontBB
from taggablebanner.const import FONTS


@dataclass
class Tag:
    element_text_path: svg.TextPath
    element_path: svg.Path
    element_bbox: svg.Rect

    @property
    def element_group(self) -> svg.G:
        return svg.G(
            id="tag",
            elements=[
                # self.element_bbox, # un-comment when you want to visualize the bbox
                self.element_path,
                svg.Text(elements=[self.element_text_path]),
            ],
        )

    @property
    def points_bbox(self) -> list[tuple[int, int]]:
        "All bbox corner points clockwise"
        return [
            (self.element_bbox.x, self.element_bbox.y),
            (self.element_bbox.x + self.element_bbox.width, self.element_bbox.y),
            (
                self.element_bbox.x + self.element_bbox.width,
                self.element_bbox.y - self.element_bbox.height,
            ),
            (self.element_bbox.x, self.element_bbox.y - self.element_bbox.height),
        ]


def build_tag(
    text: str,
    x: int,
    y: int,
    font: FontBB,
    color_class: str,
):
    font_size = max(64 - (len(text) * 2.5), 32)

    width = (font_size * font.width_size_ratio) * len(text) * 1.5
    height = font_size * font.height_size_ratio

    # bbox
    element_bbox = svg.Rect(
        x=x,
        y=y - (font_size * font.height_size_ratio),
        height=height,
        width=width,
        fill="rgb(255,255,0,0.2)",
    )

    # path
    segment_count = random.randrange(1, round(len(text) / 3) + 1, 1)
    segment_width = int(width / segment_count)
    rotation = random.randrange(-15, 15)

    segments: list[svg.ArcRel] = []
    for i in range(segment_count):
        segments.append(
            svg.ArcRel(
                dx=segment_width,  # end x
                dy=0,  # end y
                rx=random.randrange(segment_width, segment_width * 2),  # radius x
                ry=random.randrange(segment_width, segment_width * 2),  # radius y
                angle=random.randrange(160, 240),  # rotation comp to x as
                large_arc=0,  # outer arc flag
                sweep=i % 2,  # sweep flag (inverse)
            )
        )

    element_path = svg.Path(
        id=f"path-{text}",
        # stroke="white",
        fill="transparent",
        d=[
            svg.M(
                x=x,  # root x position of tag
                y=y,  # root y position of tag
            ),
            *segments,
        ],
        transform=[svg.Rotate(rotation, x, y)],
    )

    element_text_path = svg.TextPath(
        text=text,
        href=f"#path-{text}",
        font_size=font_size,
        font_family=font.name,
        class_=color_class,
    )

    return Tag(
        element_path=element_path,
        element_text_path=element_text_path,
        element_bbox=element_bbox,
    )


def build_tag_from_minidom(element: minidom.Element) -> Tag:
    path = element.getElementsByTagName("path")[0]
    textpath = element.getElementsByTagName("textPath")[0]

    text = textpath.firstChild.nodeValue
    font_size = int(float(textpath.getAttribute("font-size")))
    font_family = textpath.getAttribute("font-family")
    font = [font for font in FONTS if font.name == font_family][0]

    transform = path.getAttribute("transform")

    x = int(path.getAttribute("d").split(" ")[1])
    y = int(path.getAttribute("d").split(" ")[2])

    width = (font_size * font.width_size_ratio) * len(text)
    height = font_size * font.height_size_ratio

    element_bbox = svg.Rect(
        x=x,
        y=y - (font_size * font.height_size_ratio),
        height=height,
        width=width,
        fill="rgb(255,255,0,0.2)",
    )

    element_path = svg.Path(
        id=path.getAttribute("id"),
        fill="transparent",
        d=path.getAttribute("d"),
        transform=transform,
    )

    #
    element_text_path = svg.TextPath(
        text=text,
        href=textpath.getAttribute("href"),
        font_size=font_size,
        font_family=font_family,
        class_=textpath.getAttribute("class"),
    )

    return Tag(
        element_path=element_path,
        element_text_path=element_text_path,
        element_bbox=element_bbox,
    )
