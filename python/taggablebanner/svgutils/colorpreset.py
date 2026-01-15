# buildin modules
from dataclasses import dataclass

# thirdparty modules
import svg


@dataclass
class ColorPreset:
    name: str
    fill_light_start: str
    fill_light_stop: str
    fill_dark_start: str
    fill_dark_stop: str
    glow_dark: str | None = None
    glow_light: str | None = None

    def __str__(self):
        return (
            f".{self.name} {{"
            f"fill: var(--svg-gradient-{self.name});"
            f"text-shadow: 0 0 4px var(--svg-glow-{self.name});"
            "}"
        )

    @property
    def gradient_light(self) -> str:
        return (
            f"--svg-gradient-{self.name}: url(#gradient-{self.name}-light);"
            f"--svg-glow-{self.name}: {self.glow_light};"
        )

    @property
    def gradient_dark(self) -> str:
        return (
            f"--svg-gradient-{self.name}: url(#gradient-{self.name}-dark);"
            f"--svg-glow-{self.name}: {self.glow_dark};"
        )

    @property
    def gradient_elements(self) -> svg.G:
        light = svg.LinearGradient(
            id=f"gradient-{self.name}-light",
            gradientTransform=svg.Rotate(90),
            elements=[
                svg.Stop(offset="0%", stop_color=self.fill_light_start),
                svg.Stop(offset="100%", stop_color=self.fill_light_stop),
            ],
        )

        dark = svg.LinearGradient(
            id=f"gradient-{self.name}-dark",
            gradientTransform=svg.Rotate(90),
            elements=[
                svg.Stop(offset="0%", stop_color=self.fill_dark_start),
                svg.Stop(offset="100%", stop_color=self.fill_dark_stop),
            ],
        )

        return svg.G(
            elements=[
                light,
                dark,
            ]
        )
