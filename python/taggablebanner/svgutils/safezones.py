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
        if distance >= self.r:
            return False

        return True

    @property
    def element(self) -> svg.Circle:
        return svg.Circle(
            cx=self.cx,
            cy=self.cy,
            r=self.r,
            fill="rgb(255,0,0,0.2)",
        )


class SafeZoneRect(SafeZone):
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill = "rgb(255,0,0,0.2)"

    def check_if_point_in(self, x, y):
        if x < self.x:
            return False

        if x > self.x + self.width:
            return False

        if y < self.y:
            return False

        if y > self.y + self.height:
            return False

        return True

    @property
    def element(self) -> svg.Rect:
        return svg.Rect(
            x=self.x,
            y=self.y,
            width=self.width,
            height=self.height,
            fill=self.fill,
        )
