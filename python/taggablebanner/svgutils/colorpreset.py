from dataclasses import dataclass


@dataclass
class ColorPreset:
    name: str
    fill_light: str
    fill_dark: str
    stroke_light: str | None = None
    stroke_dark: str | None = None

    def __str__(self):
        return f".{self.name} {{fill: light-dark({self.fill_light}, {self.fill_dark});stroke: light-dark({self.stroke_light},{self.stroke_dark});stroke-width:2px;paint-order: stroke fill;}}"
