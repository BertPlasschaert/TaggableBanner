import svg

from pathlib import Path


output_svg = Path("bbox.svg")

name = "BerT"
font_size = 36


text = svg.Text(
    text=name,
    font_size=font_size,
    fill="black",
    x=0,
    y=font_size,
)

bbox = svg.Rect(
    x=0,
    y=0,
    fill="red",
    height=font_size,
    width=(font_size / 2) * len(name),
)


def draw() -> svg.SVG:
    return svg.SVG(
        overflow="hidden",
        viewBox=svg.ViewBoxSpec(
            0,
            0,
            500,
            500,
        ),
        elements=[
            bbox,
            text,
        ],
    )


output = draw().as_str()
with open(output_svg, "w") as f:
    f.write(output)
