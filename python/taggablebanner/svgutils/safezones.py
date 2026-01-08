import math

import svg


class SafeZone:
    pass


class SafeZoneCircle(SafeZone):
    def __init__(self, cx: int, cy: int, r: int):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.fill = "rgb(255,0,0,0.2)"

    def check_if_point_in(self, x, y):
        distance = math.dist((self.cx, self.cy), (x, y))
        if distance <= self.r:
            return True

        return False

    @property
    def element(self) -> svg.Circle:
        return svg.Circle(
            cx=self.cx,
            cy=self.cy,
            r=self.r,
            fill="rgb(255,0,0,0.2)",
        )


class SafeZoneSquare(SafeZone):
    def __init__(self, x: int, y: int, width):
        self.x = x
        self.y = y
        self.width = width
        self.fill = "rgb(255,0,0,0.2)"

    def check_if_point_in(self, x, y):
        corners = (
            (self.x, self.y),
            (self.x + self.width, self.y),
            (self.x + self.width, self.y + self.width),
            (self.x, self.y + self.width),
        )

        buffer = 20
        count = 0
        for corner in corners:
            distance = math.dist((corner[0], corner[1]), (x, y)) - buffer
            if distance <= self.width:
                count += 1

        if count >= 3:
            return True

        return False

    @property
    def element(self) -> svg.Rect:
        return svg.Rect(
            x=self.x,
            y=self.y,
            width=self.width,
            height=self.width,
            fill=self.fill,
        )
