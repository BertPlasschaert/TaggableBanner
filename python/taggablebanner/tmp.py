from pathlib import Path
from math import sin, cos, radians
from pprint import pprint

import svg


px = 20
py = 20
w = 40
h = 20


points = [
    (px, py),
    (px, py + h),
    (px + w, py + h),
    (px + w, py),
]


m1 = [
    [1, 0, -px],
    [0, 1, -py],
    [0, 0, 1],
]

transform_rad = radians(-45)

m2 = [
    [cos(transform_rad), -sin(transform_rad), 0],
    [sin(transform_rad), cos(transform_rad), 0],
    [0, 0, 1],
]


m3 = [
    [1, 0, px],
    [0, 1, py],
    [0, 0, 1],
]


def multiply_matrix(m1, m2):
    dimension = len(m1)

    matrix_result = [[0] * dimension for i in range(dimension)]
    for row in range(dimension):
        for column in range(dimension):
            intermediate_cell = list()
            for i in range(dimension):
                intermediate_cell.append((m1[row][i] * m2[i][column]))
            matrix_result[row][column] = sum(intermediate_cell)

    return matrix_result


result_m = multiply_matrix(multiply_matrix(m3, m2), m1)

# transform_m = multiply_matrix(t1_m, m3)
# mr = multiply_matrix(mr, m3)
# pprint(transform_m[0])
# pprint(transform_m[1])
# pprint(transform_m[2])

print("--" * 8)

pprint([result_m[0][0], result_m[0][1], result_m[0][2]])
pprint([result_m[1][0], result_m[1][1], result_m[1][2]])
pprint([result_m[2][0], result_m[2][1], result_m[2][2]])

print("--" * 8)


og_corners = list()
for corner in points:
    og_corners.append(svg.Circle(cx=corner[0], cy=corner[1], r=2, fill="black"))

transformed_corners = list()
for corner in points:
    point_m = [
        [1, 0, corner[0]],
        [0, 1, corner[1]],
        [0, 0, 1],
    ]

    print("point in:")
    pprint(point_m[0])
    pprint(point_m[1])
    pprint(point_m[2])

    transformed_point = multiply_matrix(result_m, point_m)

    print("point out:")
    pprint(transformed_point[0])
    pprint(transformed_point[1])
    pprint(transformed_point[2])
    print("-\-|-" * 8)

    transformed_corners.append(
        svg.Circle(
            cx=transformed_point[0][2],
            cy=transformed_point[1][2],
            r=2,
            fill="pink",
        )
    )


rect = svg.Rect(
    x=px,
    y=py,
    fill="green",
    width=w,
    height=h,
)
rect_t = svg.Rect(
    x=px,
    y=py,
    fill="red",
    width=w,
    height=h,
    transform=[
        svg.Matrix(
            result_m[0][0],
            result_m[1][0],
            result_m[0][1],
            result_m[1][1],
            result_m[0][2],
            result_m[1][2],
        )
    ],
)
rect_r = svg.Rect(
    x=px,
    y=py,
    fill="yellow",
    width=w,
    height=h,
    transform=[svg.Rotate(-45, px, py)],
)

o = svg.Circle(
    cx=0,
    cy=0,
    r=2,
    fill="black",
)

r = svg.SVG(
    overflow="hidden",
    viewBox=svg.ViewBoxSpec(
        -200,
        -200,
        400,
        400,
    ),
    elements=[
        o,
        rect,
        rect_t,
        rect_r,
        *og_corners,
        *transformed_corners,
    ],
)

output = r.as_str()

output_svg = Path("transform.svg")
with open(output_svg, "w") as f:
    f.write(output)

# pprint()
