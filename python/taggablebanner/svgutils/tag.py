# stdlib modules
from dataclasses import dataclass
from xml.dom import minidom
import random
import math

# thirdparty modules
import svg

# tool modules
from taggablebanner.svgutils.fontbb import FontBB
from taggablebanner.const import FONTS


@dataclass
class Tag:
    element_text_path: svg.TextPath
    element_path: svg.Path
    element_bbox: svg.Rect

    def _bbox_points(self) -> list[list[float]]:
        """
        All bbox corner points and center point, without rotation.

        These points represent the boundingbox of the tag, but without the
        random rotation applied.
        """
        return [
            [self.element_bbox.x, self.element_bbox.y],
            [self.element_bbox.x + self.element_bbox.width, self.element_bbox.y],
            [
                self.element_bbox.x + self.element_bbox.width,
                self.element_bbox.y + self.element_bbox.height,
            ],
            [self.element_bbox.x, self.element_bbox.y + self.element_bbox.height],
            # center point
            [
                self.element_bbox.x + self.element_bbox.width / 2,
                self.element_bbox.y + self.element_bbox.height / 2,
            ],
        ]

    def _bbox_transform_matrix(self) -> list[list[float]]:
        """Calculate the transformation matrix from the tags' generated elements."""
        px = self.element_bbox.x
        py = self.element_bbox.y - self.element_bbox.height

        m_undo_translation = [
            [1, 0, -px],
            [0, 1, -py],
            [0, 0, 1],
        ]

        rot_deg = 0
        for transform in self.element_path.transform:
            if isinstance(transform, svg.Rotate):
                rot_deg = transform.a

        rot_rad = math.radians(rot_deg)
        m_rotation = [
            [math.cos(rot_rad), -math.sin(rot_rad), 0],
            [math.sin(rot_rad), math.cos(rot_rad), 0],
            [0, 0, 1],
        ]

        m_redo_translation = [
            [1, 0, px],
            [0, 1, py],
            [0, 0, 1],
        ]

        transform_matrix = multiply_matrix(
            multiply_matrix(m_redo_translation, m_rotation),
            m_undo_translation,
        )

        return transform_matrix

    @property
    def element_group(self) -> svg.G:
        """Group svg element with the path and text element."""
        return svg.G(
            id="tag",
            elements=[
                # self.element_bbox,  # un-comment when you want to visualize the bbox
                self.element_path,
                svg.Text(elements=[self.element_text_path]),
            ],
        )

    @property
    def bbox_points_transformed(self) -> list[list[float]]:
        """
        All bbox corner points and center point, with rotation applied.

        These points represent the boundingbox of the tag, with the random
        rotation applied.
        """
        transform_matrix = self._bbox_transform_matrix()
        transformed_points: list[list[float]] = list()
        for point in self._bbox_points():
            input_matrix = [
                [1, 0, point[0]],
                [0, 1, point[1]],
                [0, 0, 1],
            ]

            result_matrix = multiply_matrix(transform_matrix, input_matrix)
            transformed_points.append([result_matrix[0][2], result_matrix[1][2]])

        return transformed_points

    @property
    def bbox_points_element(self) -> svg.G:
        """Bbox points visualizer svg element without the rotation applied."""
        elements: list[svg.Circle] = list()
        for corner in self._bbox_points():
            elements.append(
                svg.Circle(
                    cx=corner[0],
                    cy=corner[1],
                    r=5,
                    fill="green",
                )
            )

        return svg.G(elements=elements)

    @property
    def bbox_points_transformed_element(self) -> svg.G:
        """Bbox points visualizer svg element with the rotation applied."""
        elements: list[svg.Circle] = list()
        for corner in self.bbox_points_transformed:
            elements.append(
                svg.Circle(
                    cx=corner[0],
                    cy=corner[1],
                    r=5,
                    fill="yellow",
                )
            )

        return svg.G(elements=elements)


def multiply_matrix(m1, m2) -> list[list[float]]:
    """Multiply the provided two matrix"""
    dimension = len(m1)

    matrix_result = [[0] * dimension for i in range(dimension)]
    for row in range(dimension):
        for column in range(dimension):
            intermediate_cell = list()
            for i in range(dimension):
                intermediate_cell.append((m1[row][i] * m2[i][column]))
            matrix_result[row][column] = sum(intermediate_cell)

    return matrix_result


def build_tag(
    text: str,
    x: int,
    y: int,
    font: FontBB,
    color_class: str,
):
    """Construct Tag object"""
    # font_size = max(64 - (len(text) * 2.5), 32)
    font_size = max(82 - (len(text) * 2.5), 36)

    # calculate the boundingbox dimentions using the font width/height_size ratio
    width = (font_size * font.width_size_ratio) * len(text)
    height = font_size * font.height_size_ratio

    rotation = random.randrange(-15, 15)

    # bbox
    element_bbox = svg.Rect(
        x=x,
        y=y - (font_size * font.height_size_ratio),
        height=height,
        width=width,
        transform=[svg.Rotate(rotation, x, y)],
        fill="transparent",
    )

    # path
    segment_count = random.randrange(1, round(len(text) / 3) + 1, 1)
    segment_width = int(width / segment_count)

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
    """Construct Tag object from a minidom tag group element."""
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
        transform=transform,
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
