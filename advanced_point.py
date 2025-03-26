from Color_point import ColorPoint, PointException





class AdvancedPoint(ColorPoint):
    COLORS = ["red", "blue", "green", "yellow", "black", "white", "gold"]


    def __init__(self, x, y, color):
        """
        Initializes an advanced point with color and makes sure color is valid

        """

        if color not in self.COLORS:
            raise TypeError(f"Invalid color, must be one of {self.COLORS}")
        self._x = x
        self._y = y
        self._color = color


    @property
    def x(self):
        """
        Gets the x value

        """
        return self._x

    @x.setter
    def x(self, value):
        """
        Sets the x value

        """
        self._x = value

    @property
    def y(self):
        """
        Gets the y value

        """
        return self._y

    @property
    def color(self):
        """
        Gets the color value

        """
        return self._color

    @classmethod
    def add_color(cls, color):
        """
        Adds a new color to the list

        """
        cls.COLORS.append(color)


    @staticmethod
    def from_tuple(coordinate, color="red"):
        """
        Creates a point (x, y) and optional color

        """
        x, y = coordinate
        return AdvancedPoint(x, y, color)

    @staticmethod
    def distance_2_points(p1, p2):
        """
        Calculates dist between two points
        """
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


    def distance_to_other(self, p):
        """
        Calculates dist to another point

        """
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5



AdvancedPoint.add_color("rojo")
p = AdvancedPoint(1, 2, "rojo")
print(p.x)
print(p)
print(p.distance_orig())
p2 = AdvancedPoint.from_tuple((3, 2))
print(p2)
print(AdvancedPoint.distance_2_points(p, p2))
print(p.distance_to_other(p2))
