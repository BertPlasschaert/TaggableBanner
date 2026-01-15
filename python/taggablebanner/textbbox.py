import svg

from pathlib import Path

output_svg = Path("text_bbox.svg")

name = "BerT"
font_size = 36


draw_fonts():
    text = svg.Text(
        text=name,
        font_size=font_size,
        fill="black",
        x=0,
        y=font_size,
    )


def draw() -> svg.SVG:
    font_elements = draw_fonts()

    return svg.SVG(
        overflow="hidden",
        viewBox=svg.ViewBoxSpec(
            0,
            0,
            500,
            500,
        ),
        elements=[
            *font_elements,
        ],
    )


if __name__ == "__main__":
    with open(output_svg, "w") as f:
        f.write(draw().as_str())
