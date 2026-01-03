import svg

from svgutils.fontbb import FontBB


class TextBounded:
    def __init__(
        self,
        text: str,
        x: int,
        y: int,
        rotation: int,
        font: FontBB,
        font_size: int,
        color_class: str,
    ):
        self.text = text
        self.x = x
        self.y = y
        self.rotation = rotation
        self.font = font
        self.font_size = font_size

        self.width = (self.font_size * self.font.width_size_ratio) * len(self.text)
        self.height = self.font_size * self.font.height_size_ratio
        self.color_class = color_class

    @property
    def element_text(self) -> svg.Text:
        return svg.Text(
            id="tag",
            text=self.text,
            font_family=self.font.name,
            x=self.x,
            y=self.y,
            font_size=self.font_size,
            transform=svg.Rotate(
                self.rotation,
                self.x,
                self.y,
            ),
            class_=self.color_class,
        )

    @property
    def element_bbox(self) -> svg.Text:
        return svg.Rect(
            x=self.x,
            y=self.y - (self.font_size * self.font.height_size_ratio),
            height=self.height,
            width=self.width,
            fill="rgb(255,255,0,0.2)",
        )

    @property
    def points_bbox(self) -> list[tuple[int, int]]:
        "All bbox corner points clockwise"
        return [
            (self.x, self.y),
            (self.x + self.width, self.y),
            (self.x + self.width, self.y - self.height),
            (self.x, self.y - self.height),
        ]
