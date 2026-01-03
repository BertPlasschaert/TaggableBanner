from dataclasses import dataclass


@dataclass
class ColorPreset:
    name: str
    light: str
    dark: str

    def __str__(self):
        return f".{self.name} {{fill: light-dark({self.light}, {self.dark});}}"
